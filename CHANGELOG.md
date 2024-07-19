# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project uses ~~[Semantic Versioning](https://semver.org/spec/v2.0.0.html)~~ [Calendar Versioning](https://calver.org/).

## [v2024.07.19](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v2024.07.14...v2024.07.19) (2024-07-19)


### 🚀 Features

* upgrade wagtail to version 6.1 ([#531](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/531)) ([a84005c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a84005caeb622167f76aff3efdc661151d2ab4e2))
* bump @babel/* packages to 7.24.x ([0503453](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/05034531e4fca6e5923f66b6f3c5d76b930890fb))
* bump autoprefixer from 10.4.17 to 10.4.19 ([5d9b1a8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5d9b1a8533481b87927669548a65db516bb43065))
* bump bootstrap (^5.3.2 → ^5.3.3) ([62bbddc](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/62bbddcb5c6e05364dd1aef5fe319826ca1068ee))
* bump css-loader (^6.10.0 → ^7.1.2) ([9d4d94a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9d4d94a7915a4609c058d9660fcccd6ffd91e5e2))
* bump cssnano (^6.0.3 → ^7.0.4) ([2293979](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2293979e18f03e6282f292c5eb51add8ef13bb4f))
* bump eslint-plugin-prettier (^5.1.3 → ^5.2.1) & eslint-webpack-plugin (^4.0.1 → ^4.2.0) ([8f0b12d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8f0b12de9a0fccba201eedce3a843cb92aae1cd4))
* bump mini-css-extract-plugin (^2.8.0 → ^2.9.0) & sass-loader (^14.0.0 → ^14.2.1) ([80e0e81](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/80e0e8139b8bb61c6191e9eaa19e775640cba645))
* bump Node.js from 20 to 22 ([ab3f9e2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ab3f9e24b1b9f9e90cceb083c0a11ae4bb60831a))
* bump prettier and stylelint (& friends) to latest versions ([c477b4e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c477b4ef9d71d07ff56801300c0c8ceb5384c4d4))
* bump webpack-dev-server (^4.15.1 → ^5.0.4) ([7d8da94](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7d8da94b05e21d2d461d356831f7447e28e7b446))
* bump whitenoise (6.6.0 -> 6.7.0) ([7cb917a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7cb917ad7ba61a959776d0e0a8e3b537c607aa4e))
* update copy-webpack-plugin, postcss-custom-properties, postcss-loader & webpack to latest versions ([9d67de2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9d67de25cb3b822495da9650205f73915a78b864))
* update crispy-bootstrap5 (2023.10 -> 2024.2) ([a8672e8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a8672e83ca645d861ac32e20669e3561e5405d2e))
* update Node Engine spec and use .nvmrc to specify Node version ([f9bf437](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f9bf4372a2135963e1c5ec39bf6c8e266c10fb75))
* update several outdated python dependencies ([8f7d782](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8f7d782d027102b2e94d2c413ee5031ffac8b13a))


### 🐛 Bug Fixes

* address https://avd.aquasec.com/nvd/cve-2024-6345 by updating setuptools ([5ea3fc9](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5ea3fc9c94098b570c51a7ba1455faf0600ff8a2))
* ensure sass is not updated, for now ([6b65631](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6b656316d46053606a321afcacd845c44776c23f)), closes [#499](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/499)
* pin Node 22 to 22.4, because 22.5 has issues ([2ee825f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2ee825fdb4f931959b3c972e345a1030f0faf706))


### 💄 Styling

* fix formatting with prettier ([bb9fd5f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bb9fd5f44745d5573621531023e48970261819c0))


### ♻️ Code Refactoring

* update .editorconfig by ensuring that html indentation is 4 spaces ([a78b732](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a78b732104bff43af048d3eeb6cc180a0ec1dc44))


### ⚙️ Build System

* **deps:** update dependency boto3 to v1.34.145 ([#485](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/485)) ([5ec18df](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5ec18df60e8d953d778ad85005e34df825215901))
* **deps:** update dependency commitizen to v3.27.0 ([#517](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/517)) ([43b792d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/43b792d23814d7dda21e9f666f607b188c712c14))
* **deps:** update dependency django-anymail to v10.3 ([fb67e80](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fb67e8065634a86a9c73e781eae1274195e0a381))
* **deps:** update dependency django-crispy-forms to v2.2 ([#521](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/521)) ([4e1b11a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4e1b11aa5b3bb8e447453f301109d8fb1a2603f9))
* **deps:** update dependency mkdocs-glightbox to ^0.4.0 ([#522](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/522)) ([13fb29a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/13fb29aa41d18e44b98cd644aedd4b65c8dd1705))
* **deps:** update dependency mkdocs-material to v9.5.29 ([#529](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/529)) ([e0b4158](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e0b41588bfc285ed546997a8de00f135c9d20ad0))
* **deps:** update dependency pydantic to v2.8.2 ([#523](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/523)) ([bc809a5](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bc809a58d92792f0e50392e861bce7ad763cb676))
* **deps:** update dependency pytest-django to v4.8.0 ([#502](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/502)) ([35ff3e2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/35ff3e289202f301f93e1eea20fbcfc7455086ec))
* **deps:** update dependency pytest-factoryboy to v2.7.0 ([#524](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/524)) ([f309b59](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f309b59c89577e00f427db5c519fb95996801801))
* **deps:** update dependency pytest-mock to v3.14.0 ([#525](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/525)) ([dc65704](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/dc6570459ee84f1c16354e06b9e7c63be2142e6d))
* **deps:** update dependency pytest-xdist to v3.6.1 ([#526](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/526)) ([fc98fc4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fc98fc46583559db9f1b1eb77534112a62eaddc1))
* **deps:** update dependency ruff to v0.5.2 ([#530](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/530)) ([575c3de](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/575c3def92995bcc83aa7748c981ad49b547ebcc))
* **deps:** update dependency sentry-sdk to v1.45.0 ([#528](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/528)) ([7814070](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7814070873b92a47aff05c11066b3c1a1513f393))
* **deps:** update dependency wagtail-factories to v4.2.1 ([#532](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/532)) ([1953428](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1953428e5e003cb5aa2eb76a48028e1fbb0a4b19))

### 👷 CI/CD

* ensure that [@renovate-bot](https://github.com/renovate-bot) doesn't automerge wagtail _minor_ releases ([619b746](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/619b746ebbde2d4602acb5668b5d881d8fd36798))


## [v2024.07.14](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v2023.12.28...v2024.07.14) (2024-07-14)


### 🚀 Features

* bump bootstrap from 5.3.2 to 5.3.3 ([849a88d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/849a88d7c1c029ef0778ab3d3d7b44412134ef7d))
* bump gunicorn from v21 to v22 ([6cb85bd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6cb85bd6a3772f4b5368c71a8e8c913d84666a7f))
* bump Node.js from 18 to 20 ([4fd67ee](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4fd67ee61a9c00fa299eda7091e125506a9162f1))
* bump poetry version from 1.6.1 to 1.8.3 ([b48e6d1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b48e6d104b2a7968c6fc228a2d9fbe23c3d5e67c))
* bump wagtail from 5.2 to 6.0 ([238cca3](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/238cca3774bd3811e9d1655b90663c9e69791c01))
* speed up CI/CD ([2e0fb3a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2e0fb3a2d6c00a3571a9ea124ee00f59bf4b4a84))
* use latest versions of black & ruff ([7d33907](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7d339072666e8b27d099a5e9bf3a52e56a9a62df))

### 🐛 Bug Fixes

* ensure black doesn't fail on tasks.py ([73f8b3b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/73f8b3b79fc534134ca1daeda236762c639e6553))
* ensure djLint is happy with all templates ([9a30799](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9a30799e80c39dba73650b3922626c90929b23d4))
* ruff config ([67a17e3](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/67a17e3df4d1334d263f1291f7c81339f35509ff)), closes [#513](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/513)
* webpack dev server proxy config ([01ba0a0](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/01ba0a0c4e3d510cd2e6457ded64ad7084823ea5)), closes [#512](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/512)

### 💄 Styling

* ensure prettier is happy ([06d3f16](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/06d3f16e4990ed70819052efc9870d7f448ce987))


### ♻️ Code Refactoring

* remove `version: "3.8"` from docker-compose config ([3814b65](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/3814b65ca5225727db1fca6c4fa17b0a5c122790))
* update ruff and black pre-commit hooks ([57baa28](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/57baa284abc703e68d308a062f4a5b5931ac5aa2))


### ⚙️ Build System

* update dev dependencies for the cookiecutter-wagtail-vix project ([803179b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/803179b993a6f84cfab90825e6773abe23334fdc))


### 👷 CI/CD

* switch cookicutter-wagtail-vix from coveralls.io to codecov.io ([094dd8f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/094dd8f415889bbf37d20953401174c2bb00ac41))


## [v2024.02.10](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v2023.12.28...v2024.02.10) (2024-02-10)


### 📝 Docs

* make it immediately clear what django-rq is about ([0bd591c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0bd591cedef5771cf737ff6ee408aa421f166853))


### 🐛 Bug Fixes

* use latest NodeSource installation script ([5ddfaf7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5ddfaf745cf833800084ed13b0ece0377b9df47d)), see [nodesource/distributions/issues/1770#issuecomment-1906566381](https://github.com/nodesource/distributions/issues/1770/issues/issuecomment-1906566381) [nodesource/distributions/issues/1601#issuecomment-1906829295](https://github.com/nodesource/distributions/issues/1601/issues/issuecomment-1906829295)
* fix author formatting in `tool.poetry` section of pyproject.toml ([923acdb](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/923acdbeda7f51fcc6bdead2fe344e4744804b3e))


### ✅ Tests

* use `assertQuerySetEqual()` instead of `assertQuerysetEqual()` ([9d54735](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9d547357596ed61ddce99f9f0a727eecdd62c847))


### 👷 CI/CD

* update Node.js instalation for GitHub Actions & Gitlab CI ([a34f917](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a34f917d0a03aa0073d1f06ce24213fe552e8eee))


### ⚙️ Build System

* **deps-dev:** bump @babel/core, @babel/eslint-parser & @babel/preset-env ([4adcc48](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4adcc486a547dd036a2bb7264c131da4b96103f4))
* **deps-dev:** bump attrs (23.1.0 -> 23.2.0) ([fae7229](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fae7229dd70a9558d7e29093ade94565df0c8a92))
* **deps-dev:** bump autoprefixer, cssnano, eslint-plugin-prettier & postcss-custom-properties ([1f69c9c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1f69c9c20969a8feb4000e1d317f2bac534b4bef))
* **deps-dev:** bump black from 23.12.1 to 24.1.1 ([0045298](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/004529849f225d21d9e8e7cb193c2f07da53aabd))
* **deps-dev:** bump certifi (2023.11.17 -> 2024.2.2) ([8147312](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/81473123333127aacbd49a7e092a55c52e318c45))
* **deps-dev:** bump commitizen (3.13.0 -> 3.14.1) ([5c206a2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5c206a2f845f71efb9cc9378d6625bca9a5cdc38))
* **deps-dev:** bump cryptography (41.0.7 -> 42.0.2) ([53a6e73](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/53a6e73e72880685ef19a40710b829f41a5b2543))
* **deps-dev:** bump css-loader & mini-css-extract-plugin ([e23837a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e23837ac1d930873620e0c765be51b112daa441c))
* **deps-dev:** bump flake8 to 7.0.0 & pytest to 7.4.4 ([2cb7d43](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2cb7d43e95d1c6878fe93ea56824b29ff85c0af5))
* **deps-dev:** bump prettier (3.1.1 ❯ 3.2.5) ([076ba7f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/076ba7f0ef5dbc810406b61bc19596599b3a157e))
* **deps-dev:** bump ruff from 0.1.9 to 0.1.15 ([1a6aba3](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1a6aba353541ae5e647c2594f33f994031d3ebf8))
* **deps-dev:** bump types-python-dateutil (2.8.19.14 -> 2.8.19.20240106) ([88195e8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/88195e84dd0d3a028d803bb46a73cf65df3f3492))
* **deps-dev:** bump webpack (5.89.0 ❯ 5.90.1) ([c46c585](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c46c585b2babf4e4c900d5f4d9d6dae69aeab019))
* **deps-docs:** bump mkdocs-glightbox (0.3.5 -> 0.3.7) ([e3a0e40](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e3a0e40e0594384076066c4f655e4a78d399db5a))
* **deps-docs:** bump mkdocs-material (9.5.3 -> 9.5.9) ([912e931](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/912e931369fd0cdaf64559d389f7037d2f3745d3))
* **deps:** bump boto3 & botocore (1.34.7 -> 1.34.39) ([76e9919](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/76e99191bd1a18c1110000b37fb87631027bfb1c))
* **deps:** bump Django from 5.0 to 5.0.2 ([4df7f82](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4df7f82313954adb8282ebbfd2df9b6ec21daa60))
* **deps:** bump django-modelcluster (6.1 -> 6.2.1) ([c6fa330](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c6fa3307289a2dee031ad5f5b9b6639fa98caec5))
* **deps:** bump django-treebeard (4.7 -> 4.7.1) ([3d7298d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/3d7298d05f900b6cb1eb7e185fe5f713785f8850))
* **deps:** bump mjml (4.14.1 ❯ 4.15.3) ([edf5005](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/edf50059ffa913120524a196e6bf4b7f4e8ddfee))
* **deps:** bump pillow (10.1.0 -> 10.2.0) ([5c7af7d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5c7af7d9b503d8e561b372486100e2f59485b4af))
* **deps:** bump pillow-heif (0.14.0 -> 0.15.0) ([35098c8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/35098c8352bc7aa366e1cd4ac52aca60ac29f993))
* **deps:** bump pydantic (2.5.3 -> 2.6.1) ([e880ecf](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e880ecf336c1948be8ad6e3fcad9d6feba280e4f))
* **deps:** bump sentry-sdk from 1.39.1 to 1.40.3 ([8feb7b4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8feb7b405c8d84392087c0d6c75db78dd2051b88))
* **deps:** bump svix (1.15.0 -> 1.17.0) ([886c0e9](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/886c0e95fb789bd72450c2b3c2f42c4895e826dc))
* **deps:** bump wagtail (5.2.2 -> 5.2.3) ([0e0161b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0e0161bae3e9f2b6b97673922a6570cbe401f889))
* **deps:** bump wcwidth (0.2.12 -> 0.2.13) ([ac935fa](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ac935fa72cd4c931c4de5310feb7755f60586e33))
* **deps:** install latest release of django-mjml ([c171d38](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c171d381d61055b2ecd07bc7a0ad823f11aa4dfa))
* run `npm audit fix` ([5724555](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5724555b634f0d9484c753e0a2fd60c48fe69c98))
* update cookiecutter-wagtail-vix dev dependencies & pre-commit config ([aa21967](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/aa21967e06f33232df545d13179e7b1199a6a7db))

## [v2023.12.28](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v2021.12.09...v2023.12.28) (2023-12-28)


### ⚠ BREAKING CHANGES

* Complete rewrite of the project template to embrace a more modern stack, delivering improved performance, security, and maintainability. As part of this overhaul, I've carefully removed excess baggage and deprecated features, streamlining the template for a better development experience.

### 🚀 Features

* completely rewrite the project template ([e3d3b9d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e3d3b9d35006739c3f918ba74d0e1f8cf5510972))


### 🐛 Bug Fixes

* django secret key substitution ([6bd71d4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6bd71d4856fb75048bf65b79a2354ed006d39675))


### ♻️ Code Refactoring

* change master to main, and use Github Actions instead of Circle CI ([2d8f009](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2d8f00952df858999adc860a4a40a16e65c596ae))


### 👷 CI/CD

* add release job ([6605cc1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6605cc11177c8a52a49201df747cda90111c727b))
* update GitHub Actions and use Python 3.12 ([d3f8ed5](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d3f8ed57447992c81571064f7cf06fba9e354c00))
* use official coveralls.io Action ([e985cc8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e985cc81bc87d4a97a001b51cc549f09b2455b8e))


### ✅ Tests

* refactor imports and remove unnecessary code ([637bd94](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/637bd94930919403feb7a93be0010ddc7b39e774))
* update pytest config ([48aee8f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/48aee8fde8bf69477ecc78499b6585a42e77d24b)), closes [/github.com/pytest-dev/pytest-cov/issues/243#issuecomment-441005875](https://github.com/engineervix//github.com/pytest-dev/pytest-cov/issues/243/issues/issuecomment-441005875)


### 📝 Docs

* rewrite the README and associated docs ([a15e624](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a15e6244fe9de46d62e9637d922c0c7ca6f6315c))


### ⚙️ Build System

* **deps:** update python dependencies ([5e91e52](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5e91e52de3be3e36888b6f94472c5027202315ab))
* **deps-dev:** actually, we need commitizen ([168dd90](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/168dd9080503206cd525bbb8e5f5db5569ae1015))
* **deps:** install tomli ([bcd9885](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bcd9885e932a488b846176ad9311ef64b023d01d))


## [v2021.12.09](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v0.2.2...v2021.12.09) (2021-12-09)

### ⚙️ Build System

* **deps:** update dependency cfgv to v3.3.1 ([#377](https://github.com/engineervix/cookiecutter-wagtail-vix/pull/377)) ([15ac019](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/15ac0194fcf7a29e63472b07a1b7386fb7cd8a3c))


## [v0.2.2](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v0.2.1...v0.2.2) (2021-12-09)


### ⚙️ Build System

* **deps:** update dependency popper.js to v1.16.1 ([#351](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/351)) ([a377b65](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a377b652f73d3479fdc6b3b6842e6f06c377e01b))
* **deps:** update dependency pygments to v2.10.0 ([#371](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/371)) ([6d0e33d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6d0e33d3aebe75d25259c4c3bffea94d424d5522))


### 🐛 Bug Fixes

* add `FORCE_IMAGE_PATH` to leaflet configuration ([219c4b6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/219c4b63ab968d9eb85fdfed5171efcea3a9af2b))
* **config/settings/production.py:** determination of `LIST_OF_EMAIL_RECIPIENTS` ([f2cc88d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f2cc88d3356bf8a66f1a2f85a5a9b905b3300538))
* **config/settings/production.py:** remove `OPTIONS` key in "renditions" ([fcdc5b4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fcdc5b4a8f7c9e1404a0009fbb894011c728cac3))
* correct the fontawesome css reference in 404 template ([c705e83](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c705e83afa6c3797e2630e3868996920e099b04c))
* **deps:** update python dependencies with known security vulnerabilities ([1de19df](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1de19dfa33376b6d53cbe7815e5f40ab2351464f))

## [v0.2.1](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v0.2.0...v0.2.1) (2021-12-09)


### ⚙️ Build System

* **deps:** update dependency popper.js to v1.16.1 ([#351](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/351)) ([a377b65](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a377b652f73d3479fdc6b3b6842e6f06c377e01b))
* **deps:** update dependency pygments to v2.10.0 ([#371](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/371)) ([6d0e33d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6d0e33d3aebe75d25259c4c3bffea94d424d5522))


### 🐛 Bug Fixes

* add `FORCE_IMAGE_PATH` to leaflet configuration ([219c4b6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/219c4b63ab968d9eb85fdfed5171efcea3a9af2b))
* **config/settings/production.py:** determination of `LIST_OF_EMAIL_RECIPIENTS` ([f2cc88d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f2cc88d3356bf8a66f1a2f85a5a9b905b3300538))
* **config/settings/production.py:** remove `OPTIONS` key in "renditions" ([fcdc5b4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fcdc5b4a8f7c9e1404a0009fbb894011c728cac3))
* correct the fontawesome css reference in 404 template ([c705e83](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c705e83afa6c3797e2630e3868996920e099b04c))

## [v0.2.0](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v0.1.0...v0.2.0) (2021-08-15)


### ♻️ Code Refactoring

* rename the javascript files to main ([#268](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/268)) ([a27e2d7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a27e2d77efaf0d744f1082260c1b711010643077))


### ⚙️ Build System

* **deps-dev:** bump sqlparse to 0.4.1 ([#336](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/336)) ([ace76a6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ace76a633ec9fc95b59d26d0881183a4be91da64))
* **deps-dev:** bump typing-extensions to 3.10.0.0 ([#339](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/339)) ([bef1f39](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bef1f39dfc80e7decca9f00e5d1dadd13dd75c13))
* **deps-dev:** bump wheel to 0.37.0 ([#343](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/343)) ([8348909](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8348909459fe1587cf639292185805e79a2bd1ff))
* **deps-dev:** security upgrade urllib3 from 1.25.11 to 1.26.5 ([#289](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/289)) ([e32311a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e32311a4d6f630b0ec5d19c95314c5bcd11cb1d9))
* **deps:** bump cryptography to 3.4.7 ([#303](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/303)) ([8a669d2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8a669d2ee02a6a9a60e704a3b12faf21c8454e8c))
* **deps:** bump doc8 from 0.8.1 to 0.9.0 ([#260](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/260)) ([4c3f1ca](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4c3f1cab03e1eb5fbe7e67fc0ff89fd6e043b030))
* **deps:** bump questionary to 1.10.0 ([#331](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/331)) ([f9a2aac](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f9a2aacafe12c3726ea4e63ac01bd6e0c8d23e0d))
* **deps:** bump regex to 2020.11.13 ([#332](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/332)) ([920f76c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/920f76cf16b758dfe8974d6a4f02640f698dfa65))
* **deps:** update dependency @fortawesome/fontawesome-free to v5.15.4 ([#322](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/322)) ([5d348d5](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5d348d56a1cfaf562c66105fd4eb3a49bd48b761))
* **deps:** update dependency anyascii to v0.2.0 ([#297](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/297)) ([ed685fd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ed685fd586cdd61eab52e65c94438e640f6745d8))
* **deps:** update dependency attrs to v20.3.0 ([#298](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/298)) ([f961fc0](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f961fc0c762c61476347306acb9e5069d5a01178))
* **deps:** update dependency bleach to v3.3.1 ([#270](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/270)) ([4137e94](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4137e9455f44ba9fc77618a2855f664e5f46d8a7))
* **deps:** update dependency certifi to v2020.12.5 ([#299](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/299)) ([dbb4038](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/dbb403854d963c8cbc4cf2bea45ac0ef19674431))
* **deps:** update dependency cffi to v1.14.6 ([#271](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/271)) ([bed94e9](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bed94e912be2f5720165ae9882067a2d85f2fa67))
* **deps:** update dependency cfgv to v3.3.0 ([#300](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/300)) ([619092c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/619092cf36ffa57de2d862824bc77de3673c27d3))
* **deps:** update dependency commitizen to v2.17.13 ([#301](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/301)) ([b8da34c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b8da34c92596c5f35dd3abf05708456fa9bbd445))
* **deps:** update dependency commitizen to v2.18.0 ([#316](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/316)) ([3126697](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/31266976fe6e0c0cfd5d05dd1d190ea83ef573d2))
* **deps:** update dependency coverage to v5.5 ([#302](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/302)) ([bc58b51](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bc58b51bc6a621474f722c4ec5baf21ab80d263c))
* **deps:** update dependency deprecated to v1.2.12 ([#272](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/272)) ([c210adb](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c210adb7a19e90559d41ac64bb66467fff385927))
* **deps:** update dependency distlib to v0.3.2 ([#273](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/273)) ([e5a247b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e5a247b95e8c8e1837320c9f3aad09703fe94ab9))
* **deps:** update dependency django to v3.2.6 ([#290](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/290)) ([6e5a27e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6e5a27e83701c5895c3cb16506c4426283b600c2))
* **deps:** update dependency django-debug-toolbar to v3.2.2 ([#344](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/344)) ([240bf9f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/240bf9f8a3f6a5b8505d66df82ca55806bae9065))
* **deps:** update dependency django-maintenancemode-2 to v1.3.1 ([#304](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/304)) ([c3cce70](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c3cce709d3b0c6af726e1260c282df062eac434f))
* **deps:** update dependency django-taggit to v1.5.1 ([#305](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/305)) ([6e5a741](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6e5a74174da4bb957cd487d46bbd71276009b851))
* **deps:** update dependency django-treebeard to v4.5.1 ([#306](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/306)) ([732acc3](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/732acc30c495005910572d172ed31b26c5566669))
* **deps:** update dependency djangorestframework to v3.12.4 ([#274](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/274)) ([737651c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/737651c2bb767dd155b7df8dbd3c69fed02423d7))
* **deps:** update dependency docutils to v0.17.1 ([#307](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/307)) ([feed0b9](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/feed0b9b272dfb18ffc9e841cd86a2628bde831c))
* **deps:** update dependency et-xmlfile to v1.1.0 ([#308](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/308)) ([5b60e56](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5b60e563ae17618b0e2571af34ba65970b8afee4))
* **deps:** update dependency execnet to v1.9.0 ([#309](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/309)) ([ca2bdd8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ca2bdd862e86e178890052812d3eda059a84cea6))
* **deps:** update dependency factory-boy to v3.2.0 ([#310](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/310)) ([b9aadf8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b9aadf8e4d524fd4af10965bbfd5e86bb38de463))
* **deps:** update dependency faker to v4.18.0 ([#311](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/311)) ([7ab28db](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7ab28dbc0b28757cf7ca7b061dd3903d1a42116b))
* **deps:** update dependency flake8 to v3.9.2 ([#312](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/312)) ([bfeebfd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bfeebfd3b567153c12710fab970da745c3558d44))
* **deps:** update dependency identify to v1.6.2 ([#313](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/313)) ([b49a6a4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b49a6a43fa774ff7265cb74bfbdc8749a43445e6))
* **deps:** update dependency isort to v5.9.3 ([#291](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/291)) ([90f577b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/90f577b3bbb081b721088d5f5dc54f8bd646db7f))
* **deps:** update dependency mjml to v4.10.2 ([#296](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/296)) ([6ad8673](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6ad8673b5c6701ef662f4a7d8bfef6b770ae294e))
* **deps:** update dependency nodeenv to v1.6.0 ([#314](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/314)) ([5ff861c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5ff861caa1d48de07a5b4de317f369a65153a851))
* **deps:** update dependency packaging to v20.9 ([#315](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/315)) ([86bfb24](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/86bfb2404644db52da85ae6839a9fe0ae13d9d33))
* **deps:** update dependency pathspec to v0.9.0 ([#317](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/317)) ([079ccca](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/079ccca7bf0247312df9b6993ea9611fb2d135c4))
* **deps:** update dependency pbr to v5.6.0 ([#318](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/318)) ([fe822b7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fe822b71e035e2b41b5beba8124992c6a8431fcc))
* **deps:** update dependency pep517 to v0.11.0 ([#319](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/319)) ([c3fb6a7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c3fb6a7653f60edf67e6757455537304d883962a))
* **deps:** update dependency phonenumbers to v8.12.29 ([#275](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/275)) ([28d8c16](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/28d8c16ee7cd0d73bbc71f8857eb370380f3445a))
* **deps:** update dependency phonenumberslite to v8.12.29 ([#276](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/276)) ([5a3eacd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5a3eacda73a2175febbbaf9b4c1178358a31bd98))
* **deps:** update dependency pillow to v8.3.1 ([#277](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/277)) ([2d1477a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2d1477a35d421b49bcd8bd6c537e27f12ade70b1))
* **deps:** update dependency pip-api to v0.0.20 ([#278](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/278)) ([8d58141](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8d5814149863fcdafa4bcfa98ccb89abc866f18b))
* **deps:** update dependency pipdeptree to v2.1.0 ([#320](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/320)) ([f2b9e02](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f2b9e024ca021423dc60f40aafcbc469b628c413))
* **deps:** update dependency pre-commit to v2.14.0 ([#321](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/321)) ([c4a60dc](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c4a60dc47d96bffdb8521d9390027940e3b5c2a2))
* **deps:** update dependency prompt-toolkit to v3.0.19 ([#279](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/279)) ([c76db5b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c76db5bb4d8f932722229ac1d9ccde7036866312))
* **deps:** update dependency pycodestyle to v2.7.0 ([#323](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/323)) ([8c61bcf](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8c61bcf72c6e624d16267b2b35e74ac3e102b1e2))
* **deps:** update dependency pyflakes to v2.3.1 ([#324](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/324)) ([74037cd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/74037cd7d19c40509b5394e07cda29b90641b354))
* **deps:** update dependency pyquery to v1.4.3 ([#280](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/280)) ([e21104c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e21104cfddd758ce6e1a49efbd216125686948ac))
* **deps:** update dependency pytest to v6.2.4 ([#281](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/281)) ([5c1a069](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5c1a069c3977a82cba74b6f782f7afd1a764ba0d))
* **deps:** update dependency pytest-cov to v2.12.1 ([#325](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/325)) ([0451ce7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0451ce730cf1f9c0f6071b8a6035b12150f5926f))
* **deps:** update dependency pytest-factoryboy to v2.1.0 ([#326](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/326)) ([0fc2f26](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0fc2f26c0078ff09edaa5a41bb99e94425b64719))
* **deps:** update dependency pytest-mock to v3.6.1 ([#327](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/327)) ([50472e8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/50472e866432e3ce05693c78a40b0705af1d0c15))
* **deps:** update dependency pytest-xdist to v2.3.0 ([#328](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/328)) ([00583fd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/00583fd75c062e8ac4507ae591f2bd9408626f12))
* **deps:** update dependency python-dateutil to v2.8.2 ([#282](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/282)) ([01e5a26](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/01e5a260d04a539f94dc078dcf7852a432f0ba17))
* **deps:** update dependency python-dotenv to v0.19.0 ([#329](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/329)) ([3eae4b2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/3eae4b2bca34954f7826e4d3a1a47ef544108b70))
* **deps:** update dependency pytz to v2020.5 ([#330](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/330)) ([34b3436](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/34b34368f1f43a6b00cbce7ea28e55e31309ed80))
* **deps:** update dependency pyyaml to v5.4.1 ([#283](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/283)) ([7d99afe](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7d99afed879c1066dd0079a16e9857eb200479ce))
* **deps:** update dependency requests to v2.26.0 ([#333](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/333)) ([df535b6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/df535b6e300b820c6fc38f68da7e7cdd423cc734))
* **deps:** update dependency restructuredtext-lint to v1.3.2 ([#284](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/284)) ([c1b4794](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c1b479405af86545b904f1f5cce681f21936de8c))
* **deps:** update dependency sentry-sdk to v1.3.1 ([#292](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/292)) ([a4c9a26](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a4c9a267cdebda0f83a61175c00a8af8858fea15))
* **deps:** update dependency six to v1.16.0 ([#334](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/334)) ([dc15378](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/dc15378dbbf0ea51935678b692eb7b6aff3471a9))
* **deps:** update dependency soupsieve to v2.2.1 ([#335](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/335)) ([636f322](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/636f322ae19f7f02d913d84431b48b730f0e847b))
* **deps:** update dependency stevedore to v3.3.0 ([#337](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/337)) ([fd27a7a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fd27a7acef74f747b2d25909a6dc63073bd6e044))
* **deps:** update dependency toml to v0.10.2 ([#285](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/285)) ([41d402d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/41d402da6e834f2fc4d7f95e5a15bef97ef04585))
* **deps:** update dependency tomlkit to v0.7.2 ([#338](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/338)) ([56e482d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/56e482d0729c114c04d5debdebe656c75d2aded6))
* **deps:** update dependency typed-ast to v1.4.3 ([#286](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/286)) ([d54761f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d54761fab479639c903e7a76c6d55bfdb1c79096))
* **deps:** update dependency urllib3 to v1.26.6 ([#340](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/340)) ([05d0681](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/05d0681a64e734e6a90a7e7065bfb1ea7b7a468e))
* **deps:** update dependency virtualenv to v20.7.2 ([#341](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/341)) ([b78243c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b78243ca413c30f1f770cefb0a37b10d0f0596ff))
* **deps:** update dependency wagtail to v2.14.1 ([#342](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/342)) ([70a074e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/70a074e69a7f0a6847201faecb789b1b3b05e1d1))
* **deps:** update dependency xlsxwriter to v1.4.5 ([#345](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/345)) ([bb59e6e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bb59e6e0fac0bd0293999a0fe2006d05092a123c))


### 👷 CI/CD

* **deps:** update circleci/redis docker tag to v5.0.13 ([#294](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/294)) ([205356e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/205356e03a5d9f28f883281b1fc021d543d885c2))
* **deps:** update precommit hook commitizen-tools/commitizen to v2.18.0 ([#353](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/353)) ([2368c38](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2368c389164511cd4e55e69000b1b24e10ea6219))
* **deps:** update precommit hook pre-commit/mirrors-isort to v5.9.3 ([#295](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/295)) ([7d40104](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7d40104e1a5a1a1eabac8fbfa686358b8d800577))


### 🚀 Features

* use a Custom User Model ([#262](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/262)) ([9d0289b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9d0289b8ead36b5030a165c7c4e879fc8b750457))


### 🐛 Bug Fixes

* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([#352](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/352)) ([29146ca](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/29146cac5e6a3ac466117ee5e2d04876a3ea7691))
* **deps:** pin dependencies ([#267](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/267)) ([ae2410e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ae2410e4aa4ae196e930b5c86e0b095079a38558))
* **deps:** pin dependency @fortawesome/fontawesome-free to v5.15.3 ([#269](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/269)) ([5b25c31](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5b25c318656da8427e4c7f78e82621970c3068b6))
* update gulpfile to conform to gulp-sass v5 ([#365](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/365)) ([ab9e374](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ab9e374f7ec87d47b58ffcd9657ec51938a112fc))


### 📝 Docs

* improve docs and add contribution guidelines ([#265](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/265)) ([df26f4d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/df26f4da10dc0b3545071d903adb5ae9851e13bc))

## [v0.1.0](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v0.0.1...v0.1.0) (2021-07-21)


### ✅ Tests

* add note on embeds ([f1226bb](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f1226bb4cb3319e8a61fa3bef37363cbc3b2a5f8))
* fix broken test ([7914984](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/791498465ac319954066420276c1d4dca020a881))


### 💄 Styling

* change Instagram embed URL ([bda1a11](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bda1a118bea03da915ef824ebd393f836a368803))
* change primary colour ([0f9956c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0f9956c72c636063e6547f3f42700a5f52c31350))
* move the wagtailuserbar to the bottom-right ([82e03af](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/82e03af8ccec941a8027c32bac7b22867c83a0c8))


### 📝 Docs

* add stylelint warning ([3324737](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/3324737c8cc4b70d074648ca54cc080823fa1b9b))
* cleanup CHANGELOG ([7e0f9f6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7e0f9f68079d886b8382d136ec3d3f75c7363a9b))
* **README:** update django version after [#60](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/60) ([47e6bee](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/47e6beeea81dcbbd7dfd0e4a16f785a96136c9eb))
* **readme:** update wagtail version and link to docs ([5668133](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/566813365f12a62de919f69d9ac65f690c8d2894))
* reminder to incorporate custom sitemap and robots.txt ([731f050](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/731f050d47f1c1f87a67dca538c3dd9a3295347d))
* remove dependabot badge ([d4150f6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d4150f650afebcbccaadfcda8f15e2d0873abae1))
* Update the documentation to reflect the new changes ([88941f0](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/88941f0813d22a2646bedbc120e6af109cf02776))


### 👷 CI/CD

* add "greetings" workflow & basic issue template ([731105a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/731105a4091175c3408a326b7aaa5aa71482522d))
* add CircleCI configuration ([d4ebd31](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d4ebd31ef3074ff019c14a1ffaf56c6f55194362))
* add extra labels to dependabot PRs ([a5700b6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a5700b62cc1d8a73b5b134bf7146f8a3ef3b8493))
* add GitHub Actions and renovate ([d38716d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d38716db5a9b83d3f138cc98b34c64261a828ebf))
* add isort configuration and update pre-commit stylelint hook ([fca3755](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fca3755d95ccc743d67bc6d0fa03f36ba67fc203))
* change label from npm to javascript ([37e624c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/37e624cdc4bfca1459672ee03932e2298d99de15))
* **circleci:** just run `pytest` since we have options in `setup.cfg` ([2814ec9](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2814ec9ee92b0ab048313dddeddbc80f5395a5e2))
* **pre-commit:** update stylint config ([f6aa6d4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f6aa6d404b7c7c5901b33d7dd23500792d0cf37e))
* remove pipenv and add appropriate pip commands ([7db535c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7db535c55f9bbbf5a2b0c2b45b9baf567a174575))
* update Gitlab CI config to use gulp and node LTS ([917ee02](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/917ee029cdba4616309c79fc8bdcfdbec3f2e921))


### ⚙️ Build System

* **deps-dev:** {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([#252](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/252)) ([71430f8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/71430f81422ea686f5710b3438ff014c141dc0cf))
* **deps-dev:** bump browser-sync from 2.26.13 to 2.26.14 ([0473a02](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0473a02f45818c042f7c922457271e9026f09f1c))
* **deps-dev:** bump browser-sync in /{{cookiecutter.project_slug}} ([86cde77](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/86cde770db6df84dd088d2c3ab31ea72f67d51a2))
* **deps-dev:** bump browser-sync in /{{cookiecutter.project_slug}} ([#247](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/247)) ([e79710c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e79710c30f86f36ca9cd782789f3d8020a7d05ff))
* **deps-dev:** bump commitizen in /{{cookiecutter.project_slug}} ([f686b45](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f686b457b728596d7e3394516cab045dba893f6e))
* **deps-dev:** bump cz-emoji in /{{cookiecutter.project_slug}} ([71d1b50](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/71d1b507d2b9f33ecb95f683b609b1ca4af79449))
* **deps-dev:** bump grunt-stylelint in /{{cookiecutter.project_slug}} ([0c92a91](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0c92a914cb53788c39bbf2b7a8cf282941fdd67a))
* **deps-dev:** bump holderjs in /{{cookiecutter.project_slug}} ([7ff83e3](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7ff83e376721c4523b29eb15949bade9c6d40a43))
* **deps-dev:** bump holderjs in /{{cookiecutter.project_slug}} ([48f84de](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/48f84de0d7b8ce4283fa49ab84cbbea31b9177b9))
* **deps-dev:** bump node-sass in /{{cookiecutter.project_slug}} ([6067ddc](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6067ddcdbd624572e29c60d1e12b854877291f74))
* **deps-dev:** bump some dependedncies ([34106b1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/34106b10f053d6ac07bf64eb9ade722829dc307b)), closes [#214](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/214) [#217](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/217)
* **deps-dev:** bump stylelint in /{{cookiecutter.project_slug}} ([864f1ea](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/864f1ea9a99c35375ac48d7c0fbf4b602b6c6e01))
* **deps-dev:** bump stylelint in /{{cookiecutter.project_slug}} ([fce1aee](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/fce1aee1653f88aa07b33a3e7964fadaa766bea6))
* **deps-dev:** bump stylelint-config-standard ([2a9a7d0](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2a9a7d05e6e7e506a5576f8d0a7a0f2cd7e83420))
* **deps-dev:** bump urllib3 to 1.26.5 ([a92f915](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a92f915ad5c8f4df0adb766990401db0876919c4))
* **deps-dev:** install invoke and isort[requirements_deprecated_finder] ([10b0591](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/10b0591cc403a1b2ce9a8da507bac99043941d5b))
* **deps-dev:** update cryptography to >3.3 ([b476451](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b4764518fbf5586ee120f656182e75ade51ce372))
* **deps-dev:** update dependencies and ensure compatibility ([1baa566](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1baa56620f72180b92f2b1913e8a283d9695beaa))
* **deps:** add django-anymail 8.4 & django-mjml 0.11.0 ([4a9ed5e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4a9ed5ed9136e90cef212999c70557870f774b29))
* **deps:** add fresh yarn.lock file ([03b008d](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/03b008d23d1d988039bb90982fb59ddbc2dcc344))
* **deps:** bump a number of dependencies ([1bab230](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1bab23018aab081ed9f568ef31afaba91c1f0c7a))
* **deps:** bump bootswatch in /{{cookiecutter.project_slug}} ([53bd046](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/53bd04606a6ea3115504e0111241cd7ddaf50f02))
* **deps:** bump cookiecutter from 1.7.2 to 1.7.3 ([#212](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/212)) ([7b14c45](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7b14c4538e851354c6e50c15c5ef633cdc5301ff))
* **deps:** bump cryptography from 3.3.1 to 3.3.2 and django from 3.1.6 to 3.1.7 ([d953016](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d95301627fcb828f2623996cbcf48bcb118fb070))
* **deps:** bump django from 3.1.4 to 3.1.5 ([191d821](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/191d821db652104f3ba9ab037dda5635e5db9802))
* **deps:** bump django-debug-toolbar from 3.1.1 to 3.2 ([09689c5](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/09689c5e4b0ad9d9cdf1c3e98abf28997726b206))
* **deps:** bump django-extensions from 3.0.9 to 3.1.0 ([9033550](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/903355000d47776b2720a7ea4f8648e9a7c3d269))
* **deps:** bump django-extensions from 3.1.0 to 3.1.1 ([f9a6865](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f9a686546d044791fa070880aa9e7e63a2469d36))
* **deps:** bump django-extensions from 3.1.1 to 3.1.3 ([ffcdedf](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ffcdedf9df8f64419261b0412e8a904f1c961684))
* **deps:** bump django-leaflet from 0.28.0 to 0.28.1 ([dcac1a4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/dcac1a4762bc9f37b482aa5681e7f296981f6862))
* **deps:** bump django-social-share from 2.0.0 to 2.1.0 ([f80b836](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f80b836be3e9c27a285616b77d5262efa3d9758a))
* **deps:** bump django-social-share from 2.1.0 to 2.1.1 ([332c5a6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/332c5a6ff4c98d7d79dc54233196013939a5b9bb))
* **deps:** bump ini in /{{cookiecutter.project_slug}} ([dd831f4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/dd831f47883cb69e6c373b5e1bd619fe8ca17993))
* **deps:** bump ipinfo from 4.0.0 to 4.1.0 ([b1ecba2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b1ecba2ab7de7ba789c01e8ee3dca70fc11594f6))
* **deps:** bump isort[requirements_deprecated_finder] ([56ad6ec](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/56ad6ec91e99d8e09c825e9d5bfd372d441884af))
* **deps:** bump isort[requirements_deprecated_finder] ([a4945bd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a4945bda5182c2e1ddd4d7b7786b933e1ae51a98))
* **deps:** bump isort[requirements_deprecated_finder] ([#254](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/254)) ([ad8b78f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ad8b78fb8b51774a882184aed6851da1eea38ca8))
* **deps:** bump outdated node packages ([2707051](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2707051f1e9ecc6b8f59d8b14ecf420c7c274194)), closes [#162](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/162) [#168](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/168) [#170](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/170) [#171](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/171) [#189](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/189) [#192](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/192) [#197](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/197) [#200](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/200) [#201](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/201) [#206](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/206) [#159](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/159)
* **deps:** bump outdated python dependencies ([6cfe024](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6cfe0240a8a6aabbbd8c233a15b2fa6532686185))
* **deps:** bump phonenumbers from 8.12.12 to 8.12.13 ([b58c30a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b58c30a00a06cc71cd30f691333f4701f75c8568))
* **deps:** bump phonenumbers from 8.12.13 to 8.12.14 ([9c6a37b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9c6a37b2dcc7563f7fb20f537f728afb793e68f2))
* **deps:** bump phonenumbers from 8.12.14 to 8.12.15 ([1ec4269](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1ec426981ab9d269619f56d5c1c19e0897810aef))
* **deps:** bump pillow from 8.1.0 to 8.1.1 ([5068b0f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5068b0fe3bffc0fc0b0d4abe6c6753765b7e2e6e))
* **deps:** bump PILLOW from 8.1.2 to 8.2.0 ([80c5bba](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/80c5bba776607d5bbbd632584186294ecd1b5cf6))
* **deps:** bump pip-tools from 5.3.1 to 5.4.0 ([f8c028b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f8c028bc62bb3c1ff7f2c20f973246ff6cc6406c))
* **deps:** bump pip-tools from 5.4.0 to 5.5.0 ([d66d276](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d66d276312a50e773437461e216e1474c85321e6))
* **deps:** bump pygments from 2.7.4 to 2.9.0 ([6fb25db](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6fb25dbff9248c460f6ec0563a4c5a5dd215ba4b))
* **deps:** bump pytest from 5.4.3 to 6.2.1 ([3b4165e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/3b4165e4ee678702207b01aaebe4d1faf4ee47f3))
* **deps:** bump pytest-django from 3.10.0 to 4.0.0 ([ea74e20](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ea74e203513a52c6c07277aa66c1cb8af1079a76))
* **deps:** bump pytest-django from 4.0.0 to 4.1.0 ([b1a5186](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b1a51868342c0de22b481a358db2b68e16260a98))
* **deps:** bump python dependencies ([d2771c3](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d2771c3d8ab5b20899815b05c57311ec04ee10dd)), closes [#221](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/221) [#222](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/222) [#223](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/223) [#224](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/224) [#225](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/225) [#227](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/227) [#230](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/230) [#231](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/231)
* **deps:** bump simplejson from 3.17.2 to 3.17.3 ([#256](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/256)) ([133c749](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/133c749ec5a862a6ed2ec9800dea7fb99782b55d))
* **deps:** bump some node and python packages ([65ff58c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/65ff58c861362347f911813da4a433e799d6a836))
* **deps:** bump some node and python packages ([27807d7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/27807d7f9abf88326f39f358c9a223559bdb34ea))
* **deps:** bump some python dependencies ([2223824](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2223824e5a45b6762b111ead133f2710b16b133c))
* **deps:** bump titlecase from 2.1.0 to 2.2.0 ([#234](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/234)) ([0cf98f8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0cf98f821130f31e7b8d7f66ff712a304b34de3d))
* **deps:** bump wagtail from 2.10.2 to 2.11.1 ([662b8f4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/662b8f48c1d5f9dd4da3bd5ec596ed103ad27495))
* **deps:** bump wagtail from 2.11.1 to 2.11.2 ([110f85a](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/110f85ac7783de56b8b2e4de97c47743dcd85892))
* **deps:** bump wagtail from 2.11.2 to 2.11.3 ([6c3430c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6c3430c4e3affe2c4ab54c0f0d19c1fff3493cd7))
* **deps:** bump wagtail from 2.12.3 to 2.12.4 ([0471be1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0471be1370203c55c0a8e660c0fa545592503277))
* **deps:** bump wagtail from 2.13.1 to 2.13.2 ([#237](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/237)) ([e1c5a6f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e1c5a6f1d89cdbaddec8bb8267be6b53beb215ab))
* **deps:** bump wagtail from 2.13.2 to 2.13.3 ([#251](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/251)) ([ba7e9ce](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ba7e9ce22203125111237bf7404533ef0c247d01))
* **deps:** bump wagtail to 2.12 ([9c6412b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9c6412b174ac077d108359bf29ea6d7d7cbdd9f7))
* **deps:** bump wagtail to 2.13.4 ([c8577ef](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/c8577ef0d3bdcd8312b54338432eff5d2c24d44b))
* **deps:** node security fixes ([4af61db](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4af61db9f79b689aa921d8080035c82eb5c96df5))
* **deps:** node security fixes ([8324b56](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/8324b566736fd9ebcd97df64a3d146b5de7e8e8f))
* **deps:** pre-commit autoupdate + bump pre-commit to 2.13.0 ([e889590](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e889590c9f1b646587c55fb90e096e03d5a864a9))
* **deps:** regenerate requirements.txt and bump pre-commit to 2.13.0 ([aadb369](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/aadb3692c18088bc2412045617483578556a26ef))
* **deps:** remove ipinfo ([58ab1a2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/58ab1a2b1fd6a65f84fa224bb70a1c9793ecdb34))
* **deps:** update dependencies ([97ef26c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/97ef26c276a039da6390d005e991bf8763c4da2a))
* **deps:** update dependency urllib3 to v1.26.5 [security] ([#261](https://github.com/engineervix/cookiecutter-wagtail-vix/issues/261)) ([47dc86e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/47dc86e293934163ad489eba5b81f8f7ffc80538))
* **deps:** update npm packages ([b4c471f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b4c471ff517074a728ed3ffb0ae85bf1330c47b1))
* **deps:** update tingle.js and stylelint-config ([0c69559](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0c6955928387373b43f0973f8ee7b34e21567802))
* **Gruntfile:** prevent `*.map` files from being copied into vendor directory ([ac17d8e](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ac17d8e1d0c50b5e7a303b82a1614a90a6ce6991))
* **Gruntfile:** specify which Bootstrap files to copy ([9d1a281](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/9d1a281d977c45cbe084a92248de47396c5ca1bb))
* incorporate commitizen-tools ([6ae6d40](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6ae6d40fbda8c17d318420641dd67809b24bedd7))
* remove Makefile ([aff96de](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/aff96dec2f9b304d961c7cc40a4c0b7a1ec2c718))
* update requirements ([bc85001](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bc85001b883d285129b1dfffe8ba56aafc8fb4bd))


### ♻️ Code Refactoring

* add correct version info in package.json ([14ec5d7](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/14ec5d7983d1dd21f5c086b3eb163c86c07b1256))
* add production settings ([0267a26](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0267a26eaccb5562d8192e0d988d1f0e196337f7))
* add python 3.9 as an option and remove un-necessary if-else statements ([434608b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/434608b3e6ed58d39caa8bc0d1f9ceecbbc54be0))
* completely remove bootswatch from the project ([55ab9fb](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/55ab9fb79327f415e7d4a42b0c73bb09674348fa))
* install holder.js as Dependency instead of DevDependecy ([2a19712](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2a19712bb05a8116f8b08c36b33b368a99c4b985))
* move conftest.py away from the project root ([bf4eabd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bf4eabd7794166141afc59aa89dd04faeebd48ea))
* regenerate .gitignore from <https://www.gitignore.io> ([256a698](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/256a6983ad9177b849d5ea8b4fc6f20882f371ed))
* remove IPINFO from the generated project ([1c019f2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1c019f220b2fb9b8a5ea2d5b899dce86cda3a956))
* reorganize configuration files ([41042f4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/41042f441a7661072775c2bcef60c5a325a4a4e4))
* update ENV files ([0045099](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/004509959ec5ac794facb8ceec56728d33074c27))
* update the fixtures ([b74e807](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b74e80758291fe567fdc5af37d68a1d66ec67470))
* update the settings to make moving to production easier ([4d76d43](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4d76d43d5fc66bdb87198a105551b56555291ed5))


### 🚀 Features

* add black config to .vscode/settings.json ([030c408](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/030c408a4d4e06b3fdffbba8aa02a917dde0f759))
* add CustomRichTextBlock with customized richtext options ([dc0b3e1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/dc0b3e1e6009f44fa8acfcf905faa9ef721eb7b2))
* add example nginx, uwsgi and celery production configs ([42465a2](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/42465a29162db246036d0d0adc250256d1e0df30))
* add MJML framework for responsive emails ([1ee3aad](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/1ee3aad4ac60ea81243dfb026e17663b99b3da19))
* improve the generated README and add CONTRIBUTING.md ([b3f9229](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b3f92293b7b3ff94336ed6b0c35b774038127f38))
* move stylelint config to package.json ([7d52106](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/7d52106b424147dc67f434832311ede60469a5fe))
* switch from grunt to gulp and use sass ([82dd014](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/82dd014991305e5079daa9b10fbdb7210014d1d5))
* task execution and automation using [`invoke`](http://www.pyinvoke.org/) ([bf8ce94](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/bf8ce94838a38118030ea4350b4af9e850e73f92))
* upgrade to Django 3.2 ([6a5e7cd](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6a5e7cd1120b543d6aa3063a3bf6f63526fcbb79))
* use setup.cfg and pyproject.toml for all python configs ([76aeb0c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/76aeb0ce0a22f2f10f4f74e982b4a0a678bdbcc6))


### 🐛 Bug Fixes

* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([2789cdb](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/2789cdbd1e77649aa28881a7992bc379c2f29ef4))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([d3e153b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/d3e153b7ef993ce6626b830f225fc034d3de8917))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([601dd58](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/601dd58e2e834c37e7cd5ca3d7c553eb1cb25212))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([95aa199](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/95aa1991c1d3bfe253adbe6f629a548dd02d1853))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([49bb503](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/49bb503dedf03858b896a0e4223c76566d3acdc4))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([f22bcf1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/f22bcf10b667a940828c6f12f4e5cd6f1e156e6f))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([a30fc47](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a30fc476968a69e4afe8bf8c7b3557775e87f5af))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([a0ec159](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/a0ec159fb77343036899fa038e0099188de0acfa))
* {{cookiecutter.project_slug}}/requirements.txt to reduce vulnerabilities ([3ffc7f4](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/3ffc7f4b188e6967fee7df94ec659abf85636858))
* add staticfiles to .gitignore ([cdbb8db](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/cdbb8db3edfd088929e27ede3edf713d0c4a71de))
* broken gitlab CI ([0d2b4f8](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0d2b4f84775c12512022feb59082436fc9c6e911))
* **circleci:** comment out `codecov/upload` task ([4ca3595](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/4ca3595dd32ceda8986521d66a2a0ac6db5da306))
* **circleci:** run `npm install --global` as root ([0e3db19](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/0e3db19205d079ab025e98a09434d77cbaa122d2))
* correct context variable in the people template ([12ae613](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/12ae613d857436602fa098bc1892d2fe5a3d738c))
* correct paths to vendor libs ([b50a628](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/b50a6286bd9277222f1815b0e024e5bc309d8556))
* **package.json:** remove trailing comma ([23767f6](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/23767f63d6f7ae50feec9d093461b457ac8b512a))
* raw print all double braces in `workflows/greetings.yml` ([2094539](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/209453948b3f7d80030b611e28167463c02ad37c))
* remove 'unknown pytest config option' and use {% raw %} in `tasks.py` ([83082c1](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/83082c1553085e236b4f466400fd6e1fda3885e8))
* remove `.envs` folder from `.gitignore` since we have sample env files in there ([e6f65e5](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/e6f65e5af9c6cf465fcceb1d9b5b4377174e1b48))
* remove `.generate(extra_kwargs={}` which is deprecated ([ec4110b](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ec4110b7974650a41690c13fa91f20d6e507ad5b))
* remove broken test in the blog app ([5a5be14](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/5a5be1413ca1646547f6c4af16d07e896d2a55ba))
* remove target "tests" from flake8 command ([91a67fa](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/91a67fa25de12f8dbd1e398e072a64e955abfda1))
* requirements.txt to reduce vulnerabilities ([40228fe](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/40228fe6bd938183467d763c57575adfb4f2e8a7))
* requirements.txt to reduce vulnerabilities ([ee9736c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/ee9736cbf10427edfa2fb04c91c02ad0c8c443f2))
* **settings:** ignore isort F405 on imports from base settings ([6aa9d08](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/6aa9d08289398d455dfe89033ff1f12caa6d931d))
* use `{% raw %}` on `{{ secrets.GITHUB_TOKEN }}` ([686f38f](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/686f38f8486913acaf908bdd766bf711b7de74bb))

## [v0.0.1](https://github.com/engineervix/cookiecutter-wagtail-vix/compare/v0.0.0...v0.0.1) (2020-10-07)


### ♻️ Code Refactoring

* add current version ([055640c](https://github.com/engineervix/cookiecutter-wagtail-vix/commit/055640c589a276dcde247e2aa58f68b76d587b31))
