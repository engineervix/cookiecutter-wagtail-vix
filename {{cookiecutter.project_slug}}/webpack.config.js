const fs = require("fs");
const path = require("path");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const CopyPlugin = require("copy-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const postcssCustomProperties = require("postcss-custom-properties");
const sass = require("sass");
const ESLintPlugin = require("eslint-webpack-plugin");
const StylelintPlugin = require("stylelint-webpack-plugin");

const projectRoot = "{{cookiecutter.project_slug}}";

// We are porting gulp-npm-dist to webpack
// https://github.com/dshemendiuk/gulp-npm-dist/blob/3eca60bdf8cfa85295cbd3cf302ce060a9b32725/index.js
const excludePatterns = [
  "*.map",
  "sandbox/**/*",
  "src/",
  "src/**/*",
  "examples/",
  "examples/**/*",
  "example/",
  "example/**/*",
  "demo/**/*",
  "spec/",
  "spec/**/*",
  "docs/",
  "docs/**/*",
  "tests/",
  "tests/**/*",
  "test/",
  "test/**/*",
  "Gruntfile.js",
  "gulpfile.js",
  "package.json",
  "package-lock.json",
  "bower.json",
  "composer.json",
  "yarn.lock",
  "webpack.config.js",
  "README",
  "LICENSE",
  "CHANGELOG",
  "*.yml",
  "*.md",
  "*.coffee",
  "*.ts",
  "*.scss",
  "*.less",
];

const vendorLibrariesToCopy = (config) => {
  config = config || {};

  const copyUnminified = config.copyUnminified || false;
  const replaceDefaultExcludes = config.replaceDefaultExcludes || false;
  const nodeModulesPath = config.nodeModulesPath || false;
  const packageJsonPath = config.packageJsonPath || false;
  let excludes = config.excludes || [];

  const workingDir = process.cwd();
  const nodeModDir = nodeModulesPath
    ? path.join(workingDir, nodeModulesPath)
    : ".";
  const packageJsonFile = packageJsonPath
    ? path.join(workingDir, packageJsonPath, "package.json")
    : "package.json";

  const buffer = fs.readFileSync(packageJsonFile);
  const packageJson = JSON.parse(buffer.toString().trim());
  const packages = [];

  if (!replaceDefaultExcludes) {
    excludes = excludes.concat(excludePatterns);
  }

  for (lib in packageJson.dependencies) {
    var mainFileDir = path.join(nodeModDir, "node_modules", lib);
    var libFiles = [];

    if (fs.existsSync(mainFileDir + "/dist")) {
      mainFileDir = mainFileDir + "/dist";
    } else {
      var depPackageBuffer = fs.readFileSync(mainFileDir + "/package.json");
      var depPackage = JSON.parse(depPackageBuffer.toString());

      if (depPackage.main) {
        var mainFile = mainFileDir + "/" + depPackage.main;
        var distDirPos;

        distDirPos = mainFile.lastIndexOf("/dist/");

        if (distDirPos !== -1) {
          mainFileDir = mainFile.substring(0, distDirPos) + "/dist";
        }
      }
    }

    function readLibFilesRecursively(target) {
      try {
        fs.readdirSync(target).forEach(function (path) {
          var fullPath = target + "/" + path;
          if (fs.lstatSync(fullPath).isDirectory()) {
            readLibFilesRecursively(fullPath);
          }
          libFiles.push(fullPath);
        });
      } catch (err) {
        console.log(err);
      }
    }

    readLibFilesRecursively(mainFileDir);

    // Includes
    packages.push(mainFileDir + "/**/*");

    //Excludes
    excludes.map(function (value) {
      packages.push("!" + mainFileDir + "/**/" + value);
    });

    if (copyUnminified === false) {
      // Delete unminified versions
      for (var i = 0; i < libFiles.length; i++) {
        var target;
        if (libFiles[i].indexOf(".min.js") > -1) {
          target = libFiles[i].replace(/\.min\.js/, ".js");
          packages.push("!" + libFiles[libFiles.indexOf(target)]);
        }
        if (libFiles[i].indexOf(".min.css") > -1) {
          target = libFiles[i].replace(/\.min\.css/, ".css");
          packages.push("!" + libFiles[libFiles.indexOf(target)]);
        }
      }
    }
  }

  return packages.filter((item) => !item.startsWith("!"));
};

const vendorLibPatterns = vendorLibrariesToCopy().map((library) => {
  const from = library.replace(
    "node_modules/intl-tel-input/**/*",
    "node_modules/intl-tel-input/build/**/*",
  );
  const context = process.cwd();
  const to = path.resolve(`./${projectRoot}/static/vendors`);
  return {
    from,
    context,
    to({ context, absoluteFilename }) {
      // excludes 'node_modules' from path
      // we don't want dist folders appearing in destination
      return `${to}/${path.relative(context, absoluteFilename)}`
        .replace("node_modules", "")
        .replace(/\/dist/, "")
        .replace(/\\dist/, "");
    },
    globOptions: {
      ignore: excludePatterns,
    },
  };
});

const options = {
  entry: {
    // multiple entries can be added here
    main: `./${projectRoot}/assets/js/main.js`,
  },
  output: {
    path: path.resolve(`./${projectRoot}/static/`),
    // based on entry name, e.g. main.js
    filename: "js/[name].min.js", // based on entry name, e.g. main.js
    clean: true,
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        {
          // Copy images to be referenced directly by Django to the "img" subfolder in static files.
          from: "img",
          context: path.resolve(`./${projectRoot}/assets/`),
          to: path.resolve(`./${projectRoot}/static/img`),
        },
        {
          // Copy favicons to be referenced directly by Django to the "ico" subfolder in static files.
          from: "ico",
          context: path.resolve(`./${projectRoot}/assets/`),
          to: path.resolve(`./${projectRoot}/static/ico`),
        },
        // Copy package.json deps to be referenced directly by Django to the "vendors" subfolder in static files.
        ...vendorLibPatterns,
      ],
    }),
    new MiniCssExtractPlugin({
      filename: "css/[name].min.css",
    }),
    new ESLintPlugin({
      failOnError: false,
      lintDirtyModulesOnly: true,
      emitWarning: true,
    }),
    new StylelintPlugin({
      failOnError: false,
      lintDirtyModulesOnly: true,
      emitWarning: true,
      extensions: ["scss"],
    }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
      {
        // this will apply to `.sass` / `.scss` / `.css` files
        test: /\.(s[ac]ss|css)$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
            },
          },
          {
            loader: "postcss-loader",
            options: {
              sourceMap: true,
              postcssOptions: {
                plugins: () => [
                  autoprefixer(),
                  postcssCustomProperties(),
                  cssnano({
                    preset: "default",
                  }),
                ],
              },
            },
          },
          {
            loader: "sass-loader",
            options: {
              sourceMap: true,
              implementation: sass,
              sassOptions: {
                outputStyle: "compressed",
              },
            },
          },
        ],
      },
      {
        // sync font files referenced by the css to the fonts directory
        // the publicPath matches the path from the compiled css to the font file
        test: /\.(woff|woff2)$/,
        include: /fonts/,
        type: "asset/resource",
        generator: {
          filename: "fonts/[name][ext]",
        },
      },
    ],
  },
  // externals are loaded via base.html and not included in the webpack bundle.
  externals: {
    // gettext: 'gettext',
  },
};

/*
  If a project requires internationalisation, then include `gettext` in base.html
    via the Django JSi18n helper, and uncomment it from the 'externals' object above.
*/

const webpackConfig = (environment, argv) => {
  const isProduction = argv.mode === "production";

  options.mode = isProduction ? "production" : "development";

  if (!isProduction) {
    // https://webpack.js.org/configuration/stats/
    const stats = {
      // Tells stats whether to add the build date and the build time information.
      builtAt: false,
      // Add chunk information (setting this to `false` allows for a less verbose output)
      chunks: false,
      // Add the hash of the compilation
      hash: false,
      // `webpack --colors` equivalent
      colors: true,
      // Add information about the reasons why modules are included
      reasons: false,
      // Add webpack version information
      version: false,
      // Add built modules information
      modules: false,
      // Show performance hint when file size exceeds `performance.maxAssetSize`
      performance: false,
      // Add children information
      children: false,
      // Add asset Information.
      assets: false,
    };

    options.stats = stats;

    // Create JS source maps in the dev mode
    // See https://webpack.js.org/configuration/devtool/ for more options
    options.devtool = "inline-source-map";

    // See https://webpack.js.org/configuration/dev-server/.
    options.devServer = {
      // Enable gzip compression for everything served.
      compress: true,
      hot: false,
      client: {
        logging: "error",
        // Shows a full-screen overlay in the browser when there are compiler errors.
        overlay: true,
      },
      static: false,
      host: "0.0.0.0",
      allowedHosts: ["all"],
      port: 3000,
      devMiddleware: {
        index: false, // specify to enable root proxying
        publicPath: "/static/",
        // Write compiled files to disk. This makes live-reload work on both port 3000 and 8000.
        writeToDisk: true,
      },
      proxy: [
        {
          context: () => true,
          target: "http://web:8000",
        },
      ],
    };
  }

  return options;
};

module.exports = webpackConfig;
