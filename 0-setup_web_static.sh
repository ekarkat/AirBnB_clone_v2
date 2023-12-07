#!/usr/bin/env bash
#setting up nginx

# Install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Getting permission to edit config files:
sudo chown -R "$USER":"$USER" /etc/nginx/sites-enabled

# Create web_static folder if it doesnt exist and shared
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Granting permission to ubuntu user for /data
sudo chown -R "ubuntu":"ubuntu" /data/

# Create a fake HTML file 
echo "Hello hbnb_static!" > /data/web_static/releases/test/index.html

# Create a symbolik link 
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Configuring nginx 
sudo rm /etc/nginx/sites-enabled/default
echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}

	location /redirect_me {
		return 301 http://justdont.tech;
	}

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-enabled/default

# Configure Error 404
echo "Ceci n'est pas une page" > /var/www/html/404.html

# Restart nginx services 
sudo service nginx restart
