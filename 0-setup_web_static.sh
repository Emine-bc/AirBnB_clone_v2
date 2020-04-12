#!/usr/bin/env bash
# script to prepare env
sudo apt-get install update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "first web page" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '35 i\   \tlocation /hbnb_static {\n\talias /data/web_static/current;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
