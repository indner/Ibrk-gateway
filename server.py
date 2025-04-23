from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
IB_GATEWAY_URL = "http://127.0.0.1:5000"  # Lokale IBKR-Gateway-Instanz

# Session prüfen
@app.route("/v1/api/iserver/auth/status", methods=["GET"])
def auth_status():
    r = requests.get(f"{IB_GATEWAY_URL}/v1/api/iserver/auth/status", verify=False)
    return jsonify(r.json()), r.status_code

# Session aktivieren
@app.route("/v1/api/iserver/reauthenticate", methods=["POST"])
def reauthenticate():
    r = requests.post(f"{IB_GATEWAY_URL}/v1/api/iserver/reauthenticate", verify=False)
    return jsonify(r.json()), r.status_code

# Account-Infos holen
@app.route("/v1/api/iserver/accounts", methods=["GET"])
def accounts():
    r = requests.get(f"{IB_GATEWAY_URL}/v1/api/iserver/accounts", verify=False)
    return jsonify(r.json()), r.status_code

# Kontostand abfragen
@app.route("/v1/api/portfolio/<account_id>/summary", methods=["GET"])
def portfolio_summary(account_id):
    r = requests.get(f"{IB_GATEWAY_URL}/v1/api/portfolio/{account_id}/summary", verify=False)
    return jsonify(r.json()), r.status_code

# Order aufgeben (Papierhandel oder Live)
@app.route("/v1/api/iserver/accounts/<account_id>/orders", methods=["POST"])
def place_order(account_id):
    order_data = request.json
    r = requests.post(f"{IB_GATEWAY_URL}/v1/api/iserver/accounts/{account_id}/orders", json=order_data, verify=False)
    return jsonify(r.json()), r.status_code

# Server starten
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
