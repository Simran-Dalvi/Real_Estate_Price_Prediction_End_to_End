# Deployment Guide (Flask + NGINX on AWS EC2)
1. Initial EC2 Setup

Update system and install required packages:
```bash
sudo apt update
sudo apt install python3-pip python3-venv
```
Clone your project:
```bash
git clone <repo link>
cd <repo link>
```

2. Create Virtual Environment
```bash
python3 -m venv bprice
source bprice/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt

Fix (if requirements.txt has Windows paths)

Edit the file:
```bash
nano requirements.txt
```

Remove Windows-specific file paths

Save: CTRL + X → Y → Enter

Then reinstall:
```bash
pip install -r requirements.txt
```

4. Run Flask Server

Important Fix (EC2 binding issue)

Edit server file:
```bash
nano server/server.py
```
Change:

app.run(host='0.0.0.0', port=5000)

Save and exit.

Run:
``` bash
python3 server/server.py
```

5. Configure EC2 Security Group

Allow inbound traffic :

Protocol: TCP
Port: 5000

6. Access Flask App

Open in browser:

http://<your-public-ip>:5000/

> Note: Flask runs on HTTP (not HTTPS)

7. Setup NGINX

Install NGINX:
```bash
sudo apt install nginx
```
Check status:
```bash
sudo service nginx status
```
Visit:

http://<your-public-ip>

You should see the NGINX Welcome Page

8. Configure NGINX for Your App

Go to config directory:
```bash
cd /etc/nginx
```
Create a new config file:
``` bash
sudo nano /etc/nginx/sites-available/flaskapp
```
Paste:
```nginx
server {
    listen 80;
    server_name _;

    root /home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client;
    index app.html;

    location / {
        try_files $uri $uri/ /app.html;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:5000/;
    }
}
```
9. Enable Configuration

Remove default config:
```bash
sudo unlink /etc/nginx/sites-enabled/default
```
Create symlink:
```bash
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/
```

10. Restart NGINX

Test config:
```bash
sudo nginx -t
```
Restart:
```bash
sudo systemctl restart nginx
```

11. Error Faced: 500 Internal Server Error

Even when backend was removed, error persisted.

Checked logs:
``` bash
sudo tail -f /var/log/nginx/error.log
```

> Error Found:Permission denied while accessing app.html
12. Fix: Permission Issue

NGINX could not access files inside /home/ubuntu/...

Grant required permissions:
```bash
sudo chmod o+rx /home
sudo chmod o+rx /home/ubuntu
sudo chmod -R 755 /home/ubuntu/Real_Estate_Price_Prediction_End_to_End
```

13. Result

Frontend started working successfully
NGINX serving static files correctly