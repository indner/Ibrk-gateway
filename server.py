from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "IBKR Gateway läuft."

@app.route("/v1/api/iserver/auth/status")
def auth_status():
    return jsonify({"authenticated": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)