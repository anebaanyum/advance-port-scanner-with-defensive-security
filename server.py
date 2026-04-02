from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/logs")
def get_logs():
    logs = []
    try:
        with open("logs.json", "r") as f:
            for line in f:
                logs.append(json.loads(line))
    except:
        pass
    return jsonify(logs)

app.run(port=5000)