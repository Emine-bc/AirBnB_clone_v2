#!/usr/bin/env bash
# script to prepare env
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "first web page" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
location="\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/ i $location" /etc/nginx/sites-available/default
sudo chown ubuntu:ubuntu -R /data/
sudo service nginx restart
