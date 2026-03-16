from flask import Flask, jsonify
import os 


app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "running", "enviroment": "minikube","arch" : "m2-arm64"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



