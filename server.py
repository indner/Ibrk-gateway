from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
IB_GATEWAY = "https://localhost:5000"

@app.route("/v1/api/iserver/auth/status", methods=["GET"])
def status():
    r = requests.get(f"{IB_GATEWAY}/v1/api/iserver/auth/status", verify=False)
    return jsonify(r.json()), r.status_code

@app.route("/v1/api/iserver/accounts", methods=["GET"])
def accounts():
    r = requests.get(f"{IB_GATEWAY}/v1/api/iserver/accounts", verify=False)
    return jsonify(r.json()), r.status_code

@app.route("/v1/api/iserver/accounts/<account_id>/orders", methods=["POST"])
def place_order(account_id):
    data = request.json
    r = requests.post(f"{IB_GATEWAY}/v1/api/iserver/accounts/{account_id}/orders", json=data, verify=False)
    return jsonify(r.json()), r.status_code

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)

@app.route('/v1/api/iserver/accounts', methods=['GET'])
def get_accounts():
    return jsonify([{"accountId": "U123456"}])  # Beispiel-Dummy-Daten

@app.route('/v1/api/portfolio/<account_id>/ledger', methods=['GET'])
def get_ledger(account_id):
    return jsonify({"totalcashvalue": [{"amount": 10000.00}]})  # Beispielwert