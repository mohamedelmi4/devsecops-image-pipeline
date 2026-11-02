from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from DevSecOps Image Pipeline!"

@app.route('/health')
def health():
    return {"status": "ok"}