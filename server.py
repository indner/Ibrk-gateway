from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

IB_GATEWAY = "https://clientportalwebapi.interactivebrokers.com"

@app.route("/v1/api/iserver/auth/status", methods=["GET"])
def status():
    r = requests.get(f"{IB_GATEWAY}/v1/api/iserver/auth/status", verify=False)
    return jsonify(r.json()), r.status_code

@app.route("/v1/api/iserver/reauthenticate", methods=["POST"])
def reauth():
    r = requests.post(f"{IB_GATEWAY}/v1/api/iserver/reauthenticate", verify=False)
    return jsonify(r.json()), r.status_code

@app.route("/v1/api/portfolio/accounts", methods=["GET"])
def accounts():
    r = requests.get(f"{IB_GATEWAY}/v1/api/portfolio/accounts", verify=False)
    return jsonify(r.json()), r.status_code

@app.route("/v1/api/portfolio/<account_id>/summary", methods=["GET"])
def summary(account_id):
    r = requests.get(f"{IB_GATEWAY}/v1/api/portfolio/{account_id}/summary", verify=False)
    return jsonify(r.json()), r.status_code

@app.route("/v1/api/iserver/account/<account_id>/orders", methods=["POST"])
def place_order(account_id):
    data = request.json
    r = requests.post(f"{IB_GATEWAY}/v1/api/iserver/account/{account_id}/orders", json=data, verify=False)
    return jsonify(r.json()), r.status_code