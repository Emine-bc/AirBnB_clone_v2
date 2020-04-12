#!/usr/bin/env bash
# script to prepare env
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "first web page" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
emp="/etc/nginx/sites-available/default"
sudo sed -i '38i\\tlocation /hbnb_static {\n\talias /data/web_static/current;\n}' $emp 
sudo chown ubuntu:ubuntu -R /data/
sudo service nginx restart
