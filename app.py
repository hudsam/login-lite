from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Default credential
DEFAULT_USERNAME = "hudsam"
DEFAULT_PASSWORD = "password"

# Template HTML
HTML_FORM = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="hudsam">
    <meta name="keywords" content="python, flask, simple login, json">
    <meta name="description" content="Login Lite Build with Python (Flask)">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta property="og:title" content="Login Lite">
    <meta property="og:type" content="application">
    <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/295/295128.png">
    <title>Login Lite</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background-color: #f4f4f9; }
        .login-container { max-width: 300px; margin: 0 auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .input-group { margin-bottom: 15px; }
        .input-group label { display: block; margin-bottom: 5px; }
        .input-group input { width: 100%; padding: 8px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .message { margin-top: 15px; text-align: center; font-weight: bold; }
        body > div > form > div:nth-child(1) > label, body > div > form > div:nth-child(2) > label { display: none; }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login Form</h2>
        <form method="POST" action="/login">
            <div class="input-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Username" autocomplete="off" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Password" autocomplete="off" required>
            </div>
            <button type="submit">Submit</button>
        </form>
        {% if message %}<div class="message" style="color: {{ 'green' if success else 'red' }};">{{ message }}</div>{% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_FORM)

@app.route('/login', methods=['POST'])
def login():
    # Support input via web form or JSON (API / cURL)
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        is_api = True
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        is_api = False

    # Credential validation
    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        message = "Success"
        success = True
        status_code = 200
    else:
        message = "Failed"
        success = False
        status_code = 401

    # Response based on accessed
    if is_api:
        return jsonify({"success": success, "message": message}), status_code
    else:
        return render_template_string(HTML_FORM, message=message, success=success), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
 