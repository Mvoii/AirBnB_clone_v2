#!/usr/bin/env bash
# sets up teh web servers for the deployment of web statics

# install nginx if not installed
sudo apt-get update
sudo apt-get install nginx

#creaet folders if not exists
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create a fake html file for testing
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
    </html>" >> /data/web_static/releases/test/index.html

# create and recreate a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx config to serve /data/web_static/current at hbnb_static/
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# restart nginx to apply changes
sudo service nginx restart
