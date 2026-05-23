# This guide for you.

### Default credential
- username : **hudsam**
- password : **password**

---

### Installation
1. clone repository : ```https://github.com/hudsam/login-lite.git```
2. change directory : ```cd login-lite```
3. create virtual environment : ```python3 -m venv .venv```
4. active virtual environment : ```source .venv/bin/activate```
5. install depedencies : ```pip install -r requirements.txt```
6. running application : ```python3 app.py```

### Tips
- use ```screen``` tool
- running background : ```nohup python3 app.py > output.log 2<&1 &```

### Troubleshooting
- error after running in background ? re-install python virtual environment (venv) dan install depedencies

---

### Testing
#####  Web UI
- open your favorite browser
- type URL : ```http://<IP ADDRESS>:8081```

#####  cURL
- open terminal
- command (Linux/MacOS) : ```curl -X POST http://<IP ADDRESS>:8081/login -H "Content-Type: application/json" -d '{"username": "<USERNAME>", "password": "<PASSWORD>"}'```
- command (Windows) : ```curl -X POST http://<IP ADDRESS>:8081/login -H "Content-Type: application/json" -d "{\"username\": \"<USERNAME>\", \"password\": \"<PASSWORD>\"}"```

##### Hydra (for Legal Penetration Testing)
- open terminal
- type command (single credential) : ```hydra -l <USERNAME> -p <PASSWORD> <IP ADDRESS> -s 8081 http-post-form "/login:username=^USER^&password=^PASS^:Failed"```

> Change the app[dot]py code on line 80 (status_code) from 401 to 301 to anticipate endless HTTP responses.
