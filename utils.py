import json
from datetime import datetime

def save_log(ip, port, status):
    log = {
        "time": str(datetime.now()),
        "ip": ip,
        "port": port,
        "status": status
    }

    with open("logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")