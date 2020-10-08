module.exports = function(grunt) {
    const sass = require('node-sass');
    require('load-grunt-tasks')(grunt);
    require("time-grunt")(grunt);
    // 1. Configuration

    grunt.initConfig({
        // pass in options to plugins, references to files, etc.

        copy: {
            fa: {
                expand: true,
                cwd: "node_modules/@fortawesome/fontawesome-free/",
                src: ["**/*", "!package.json", "!LICENSE.txt"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/fontawesome/"
            },
            animate: {
                expand: true,
                cwd: "node_modules/animate.css/",
                src: ["animate.css", "animate.min.css"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/animate/"
            },
            bootstrap: {
                expand: true,
                cwd: "node_modules/bootstrap/dist/",
                src: ["css/bootstrap.css", "css/bootstrap.min.css", "js/bootstrap.bundle.js", "js/bootstrap.bundle.min.js"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/bootstrap/"
            },
            bootstrap_notify: {
                expand: true,
                cwd: "node_modules/bootstrap-notify/",
                src: ["*.js"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/bootstrap-notify/"
            },
            bootstrap_sweetalert: {
                expand: true,
                cwd: "node_modules/bootstrap-sweetalert/dist/",
                src: ["**/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/bootstrap-sweetalert/"
            },
            bootswatch: {
                expand: true,
                cwd: "node_modules/bootswatch/dist/",
                src: ["**/*", "!**/*.scss"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/bootswatch/"
            },
            chartist: {
                expand: true,
                cwd: "node_modules/chartist/dist/",
                src: ["**/*", "!**scss/**", "!*.map"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/chartist/"
            },
            holderjs: {
                expand: true,
                cwd: "node_modules/holderjs/",
                src: ["holder.js", "holder.min.js"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/holderjs/"
            },
            imagesloaded: {
                expand: true,
                cwd: "node_modules/imagesloaded/",
                src: [
                    "imagesloaded.js",
                    "imagesloaded.pkgd.js",
                    "imagesloaded.pkgd.min.js"
                ],
                dest: "{{cookiecutter.project_slug}}/static/vendors/imagesloaded/"
            },
            jquery: {
                expand: true,
                cwd: "node_modules/jquery/dist/",
                src: ["**/*", "!*.map"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/jquery/"
            },
            jquery_countdown: {
                expand: true,
                cwd: "node_modules/jquery-countdown/dist/",
                src: ["**/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/jquery-countdown/"
            },
            js_sortable: {
                expand: true,
                cwd: "node_modules/js.sortable/",
                src: ["css/*", "js/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/js.sortable/"
            },
            lightslider: {
                expand: true,
                cwd: "node_modules/lightslider/dist/",
                src: ["css/*", "js/*", "img/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/lightslider/"
            },
            masonry_layout: {
                expand: true,
                cwd: "node_modules/masonry-layout/dist/",
                src: ["**/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/masonry-layout/"
            },
            moment: {
                expand: true,
                cwd: "node_modules/moment/min/",
                src: ["**/*", "!*.map"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/moment/"
            },
            photoswipe: {
                expand: true,
                cwd: "node_modules/photoswipe/dist/",
                src: ["**/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/photoswipe/"
            },
            select2: {
                expand: true,
                cwd: "node_modules/select2/dist/",
                src: ["**/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/select2/"
            },
            shufflejs: {
                expand: true,
                cwd: "node_modules/shufflejs/dist/",
                src: ["shuffle.js", "shuffle.min.js"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/shufflejs/"
            },
            tingle_js: {
                expand: true,
                cwd: "node_modules/tingle.js/dist/",
                src: ["**/*"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/tingle.js/"
            },
            typed_js: {
                expand: true,
                cwd: "node_modules/typed.js/lib/",
                src: ["**/*", "!*.map"],
                dest: "{{cookiecutter.project_slug}}/static/vendors/typed.js/"
            }
        },

        cssmin: {
            dist: {
                files: [{
                    expand: true,
                    cwd: "{{cookiecutter.project_slug}}/static/css/",
                    src: ["{{cookiecutter.project_slug}}.css"],
                    dest: "{{cookiecutter.project_slug}}/static/css/",
                    ext: ".min.css"
                }]
            }
        },

        uglify: {
            dist: {
                files: [{
                    expand: true,
                    cwd: "{{cookiecutter.project_slug}}/static/js/",
                    src: ["{{cookiecutter.project_slug}}.js"],
                    dest: "{{cookiecutter.project_slug}}/static/js/",
                    ext: ".min.js"
                }]
            }
        },

        watch: {
            css: {
                files: [
                    "{{cookiecutter.project_slug}}/static/css/{{cookiecutter.project_slug}}.css"
                ],
                tasks: ["cssmin"]
            },
            js: {
                files: [
                    "{{cookiecutter.project_slug}}/static/js/{{cookiecutter.project_slug}}.js"
                ],
                tasks: ["uglify"]
            }
        },

        clean: {
            dist: ["{{cookiecutter.project_slug}}/static/vendors/*"]
        },

        browserSync: {
            dev: {
                bsFiles: {
                    src: [
                        "{{cookiecutter.project_slug}}/static/css/*.css",
                        "{{cookiecutter.project_slug}}/static/js/*.js",
                        "{{cookiecutter.project_slug}}/static/vendors/**/*.css",
                        "{{cookiecutter.project_slug}}/static/vendors/**/*.js",
                        "{{cookiecutter.project_slug}}/templates/**/*.html",
                        "{{cookiecutter.project_slug}}/base/templates/**/*.html",
                        "{{cookiecutter.project_slug}}/blog/templates/**/*.html",
                        "{{cookiecutter.project_slug}}/contact/templates/**/*.html",
                        "{{cookiecutter.project_slug}}/home/templates/**/*.html",
                        "{{cookiecutter.project_slug}}/search/templates/**/*.html",
                        "{{cookiecutter.project_slug}}/**/*.py"
                    ]
                },
                options: {
                    watchTask: true,
                    proxy: "http://127.0.0.1:8000",
                    socket: {
                      domain: 'http://127.0.0.1:3000'
                  }
                }
            }
        },

        conventionalChangelog: {
          options: {
            changelogOpts: {
              // conventional-changelog options go here
              preset: 'angular'
            },
            context: {
              // context goes here
            },
            gitRawCommitsOpts: {
              // git-raw-commits options go here
            },
            parserOpts: {
              // conventional-commits-parser options go here
            },
            writerOpts: {
              // conventional-changelog-writer options go here
            }
          },
          release: {
            src: 'CHANGELOG.md'
          }
        },

        sass: {
          options: {
              implementation: sass,
              sourceMap: false
          },
          dist: {
              files: {
                  'main.css': 'main.scss'
              }
          }
        },

        stylelint: {
          options: {
            configFile: '.stylelintrc.json',
            formatter: 'verbose',
            ignoreDisables: false,
            failOnError: true,
            outputFile: '',
            reportNeedlessDisables: false,
            syntax: ''
          },
          src: [
                  '{{cookiecutter.project_slug}}/static/**/*.{css,less,scss}',
                  '!{{cookiecutter.project_slug}}/static/vendors/**/*.{css,less,scss}'
              ]
          }

    });

    // 2. Load Plugins

    grunt.loadNpmTasks("grunt-contrib-copy");
    grunt.loadNpmTasks("grunt-contrib-cssmin");
    grunt.loadNpmTasks("grunt-contrib-uglify");
    // grunt.loadNpmTasks('grunt-contrib-htmlmin');
    // grunt.loadNpmTasks('grunt-json-minification');
    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.loadNpmTasks("grunt-browser-sync");
    grunt.loadNpmTasks("grunt-newer");
    grunt.loadNpmTasks('grunt-conventional-changelog');
    grunt.loadNpmTasks('grunt-stylelint');

    // 3. Register Tasks

    // grunt.registerTask('run', function(){
    // 	console.log('I am Running');
    // });

    // grunt.registerTask('walk', function(){
    // 	console.log('I am Walking');
    // });

    // grunt.registerTask('all', ['run', 'walk']);

    grunt.registerTask("cp", ["newer:copy"]);
    grunt.registerTask("css-x", ["newer:cssmin"]);
    grunt.registerTask("js-x", ["newer:uglify"]);
    // grunt.registerTask('html-x', ['htmlmin']);
    // grunt.registerTask('json-x', ['json_minification']);
    grunt.registerTask("rm", ["clean"]);

    // grunt.registerTask('all', ['cp', 'css-x', 'js-x', 'html-x', 'json-x']);
    grunt.registerTask("all", ["cp", "css-x", "js-x"]);
    grunt.registerTask("compress", ["css-x", "js-x"]);
    grunt.registerTask('changelog', ['conventionalChangelog']);
    grunt.registerTask('sass', ['sass']);

    // default task
    grunt.registerTask("default", [
        "rm",
        "cp",
        "css-x",
        "js-x",
        "browserSync",
        "watch"
    ]);

    grunt.registerTask("sync", ["browserSync", "watch"]);
};
