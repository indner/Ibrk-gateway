from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# IBKR API läuft innerhalb des Docker-Containers lokal auf Port 5000
IBKR_BASE = "https://localhost:5000"

# SSL-Zertifikat ignorieren (Client Portal verwendet selbstsigniertes Zertifikat)
VERIFY_SSL = False

# === Authentifizierung prüfen ===
@app.route("/v1/api/iserver/auth/status", methods=["GET"])
def auth_status():
    r = requests.get(f"{IBKR_BASE}/v1/api/iserver/auth/status", verify=VERIFY_SSL)
    return jsonify(r.json()), r.status_code

# === Reauthentication (optional) ===
@app.route("/v1/api/iserver/reauthenticate", methods=["POST"])
def reauth():
    r = requests.post(f"{IBKR_BASE}/v1/api/iserver/reauthenticate", verify=VERIFY_SSL)
    return jsonify(r.json()), r.status_code

# === Konten abfragen ===
@app.route("/v1/api/portfolio/accounts", methods=["GET"])
def accounts():
    r = requests.get(f"http://localhost:5000/v1/api/portfolio/accounts", verify=False)
    return jsonify(r.json()), r.status_code

# === Ledger (Kontostand etc.) abfragen ===
@app.route("/v1/api/portfolio/<account_id>/ledger", methods=["GET"])
def ledger(account_id):
    r = requests.get(f"{IBKR_BASE}/v1/api/portfolio/{account_id}/ledger", verify=VERIFY_SSL)
    return jsonify(r.json()), r.status_code

# === Summary (alternativ zu Ledger) ===
@app.route("/v1/api/portfolio/<account_id>/summary", methods=["GET"])
def summary(account_id):
    r = requests.get(f"{IBKR_BASE}/v1/api/portfolio/{account_id}/summary", verify=VERIFY_SSL)
    return jsonify(r.json()), r.status_code

# === Order erstellen ===
@app.route("/v1/api/iserver/accounts/<account_id>/orders", methods=["POST"])
def place_order(account_id):
    data = request.json
    r = requests.post(
        f"{IBKR_BASE}/v1/api/iserver/accounts/{account_id}/orders",
        json=data,
        verify=VERIFY_SSL
    )
    return jsonify(r.json()), r.status_code

# === Server starten ===
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)