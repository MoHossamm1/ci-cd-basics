def add(a, b):
    return a + b
from flask import Flask, jsonify

def add(a, b):
    return a + b

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="hello from ci-cd-basics")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify(sum=add(a, b))

if __name__ == "__main__":
    # listen on all interfaces so Docker can expose it
    app.run(host="0.0.0.0", port=8000)
