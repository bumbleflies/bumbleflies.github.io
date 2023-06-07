#!/bin/zsh


assets_dir=../assets

download_css() {
  url=$1
  destination=$2

  echo $assets_dir/css/$destination
  wget $url -O $assets_dir/css/$destination  > /dev/null
}

echo "Installing purgecss..."
npm i --save-dev purgecss > /dev/null

echo "Installing fontforge..."
sudo apt install fontforge > /dev/null

echo "Downloading stylesheets..."
download_css https://cdn.jsdelivr.net/gh/lipis/flag-icons@6.6.6/css/flag-icons.min.css flag-icons.min.css
download_css https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css bootstrap.min.css

echo "Building site..."
(cd ..;bundle exec jekyll build)

echo "Purging CSS..."
./node_modules/.bin/purgecss --css $assets_dir/css/*.css -con ../_site/*.html ../_site/en/*.html ../_site/assets/js/*.js -o $assets_dir/css -s dropdown-toggle dropdown-item show

echo "Purging fonts..."
fontforge -script purge-fa.py ../_externals/agency-jekyll-theme/assets/css/webfonts/ ../assets/css/webfonts
