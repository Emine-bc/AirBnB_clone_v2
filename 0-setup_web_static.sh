#!/usr/bin/env bash
# script to prepare env
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown ubuntu:ubuntu -R /data/
echo "first web page" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo sed -i '35 i\   \tlocation /hbnb_static {\n\talias /data/web_static/current;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
