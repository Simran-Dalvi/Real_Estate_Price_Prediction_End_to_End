sudo apt update
sudo apt install python3-pip python3-venv
git clone <repo link>
cd <repo link>
python3 -m venv bprice
source bprice/bin/activate
pip install -r requirements.txt
if non executable because of windows file paths in the file
nano requirements.txt
remove all window file links and ctrl+X, y, Enter
pip install -r requirements.txt

python3 server/server.py

if util file needs changes in path
nano server/util.py
ctrl+X, Y, Enter

nano server/server.py
app.run(host ='0.0.0.0', port = 5000) because ec2 uses all 0.0.0.0 addresses

change security groups of ecs instance from tcp 443 to tcp 5000 

python3 server/server.py

http://<your public IP address>:5000/ because flask dosent run on https


now to the part where we host it using nginx
sudo apt install nginx
sudo service nginx status
I f we go to http://<you ip add>
ull see the nginx welcome page

now we coonect it to our own server...
nginx in lnux is in /etc/
so 
cd /etc/nginx

there are 2 files 
sites-enabled --> symlink to default
sites-available --> the default site config

go to sited available and create flaskapp
sudo nano /etc/nginx/sites-available/flaskapp
write this code

server {
    listen 80;
    server_name _;

    root /home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client;
    index app.html;

    location / {
        try_files $uri $uri/ /app.html;
    }

    location /api/ {
        rewrite ^/api(.*) $1 break;
        proxy_pass http://127.0.0.1:5000;
    }
}

now we unlink the default page in sites enabled 
sudo unlink /etc/nginx/sited-enabled/default

check if unlinked in sites-enabled by
ll

now create a symlink for the flaskapp file
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/
sudo service nginx status
sudo sytemctl stop nginx

not test it
sudo nginx -t
sudo systemctl restart nginx

it was still showing error 500 so I disconnected with backend and only run the static html file
server {
    listen 80;
    server_name _;

    root /home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client;
    index app.html;

    location / {
        try_files $uri $uri/ /app.html;
    }
}

why is the error still there. no backend is needed her. check the logs

sudo tail -f /var/log/nginx/error.log

ubuntu@ip-172-31-17-6:~$ sudo tail -f /var/log/nginx/error.log 
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [crit] 1615#1615: *4 stat() "/home/ubuntu/Real_Estate_Price_Prediction_End_to_End/client/app.html" failed (13: Permission denied), client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"
2026/03/20 19:18:25 [error] 1615#1615: *4 rewrite or internal redirection cycle while internally redirecting to "/app.html", client: 103.178.154.90, server: _, request: "GET /favicon.ico HTTP/1.1", host: "98.81.139.137", referrer: "http://98.81.139.137/"


chatgpt said something like permissions were not granted 403 forbidden

so these were the codes provided to give permission

sudo chmod o+rx /home
sudo chmod o+rx /home/ubuntu
sudo chmod -R 755 /home/ubuntu/Real_Estate_Price_Prediction_End_to_End


yay frontend is running now!

✅ Fix (simple and correct way)
🔧 Replace your /api block with THIS:
location /api/ {
    proxy_pass http://127.0.0.1:5000/;
}

👉 Notice:

❌ No rewrite

✅ Trailing / after 5000
