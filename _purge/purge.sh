#!/bin/zsh

npm i --save-dev purgecss

./node_modules/.bin/purgecss --css ../assets/css/*.css -con ../_site/*.html ../_site/en/*.html ../_site/assets/js/*.js -o ../assets/css -s dropdown-toggle dropdown-item show
