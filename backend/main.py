# backend/main.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Simulated IoT devices
devices = [
    {"id": 1, "type": "Camera", "status": "online"},
    {"id": 2, "type": "Thermostat", "status": "online"},
    {"id": 3, "type": "Door Lock", "status": "online"},
    {"id": 4, "type": "Light", "status": "online"},
]

# Security state
security = {
    "firewall_enabled": True,
    "anomaly_detection": True,
    "attacks_detected": [],
    "attacks_blocked": [],
}

# Simulated attacks
attack_types = [
    {"name": "DDoS", "description": "Distributed Denial of Service"},
    {"name": "Spoofing", "description": "Impersonation of device"},
    {"name": "Replay", "description": "Re-sending valid data maliciously"},
]

@app.route("/api/devices")
def get_devices():
    return jsonify(devices)

@app.route("/api/security")
def get_security():
    return jsonify(security)

@app.route("/api/attacks")
def get_attacks():
    return jsonify(attack_types)

@app.route("/api/attack", methods=["POST"])
def launch_attack():
    data = request.json
    attack = data.get("attack")
    target_id = data.get("target_id")
    result = {"attack": attack, "target_id": target_id, "blocked": False, "detected": False}

    # Simulate detection/blocking
    if security["firewall_enabled"] and attack == "DDoS":
        result["blocked"] = True
        security["attacks_blocked"].append(result)
    elif security["anomaly_detection"] and attack in ["Spoofing", "Replay"]:
        result["detected"] = True
        security["attacks_detected"].append(result)
    else:
        # Randomly affect device
        for d in devices:
            if d["id"] == target_id:
                d["status"] = "compromised"
        security["attacks_detected"].append(result)
    return jsonify(result)

@app.route("/api/security/toggle", methods=["POST"])
def toggle_security():
    data = request.json
    if "firewall_enabled" in data:
        security["firewall_enabled"] = data["firewall_enabled"]
    if "anomaly_detection" in data:
        security["anomaly_detection"] = data["anomaly_detection"]
    return jsonify(security)

if __name__ == "__main__":
    app.run(debug=True)