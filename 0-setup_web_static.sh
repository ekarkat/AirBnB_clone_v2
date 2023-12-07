#!/usr/bin/env bash
#setting up nginx

# Install Nginx
apt-get update
apt-get install -y nginx

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
echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html;

	add_header X-Served-By $(hostname) always;

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
}" > /etc/nginx/sites-available/default

# Restart nginx services 
sudo service nginx restart
