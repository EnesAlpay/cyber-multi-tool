import json, os
from datetime import datetime

LOG_DIR = "logs"

def log(module, data):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    log_file = os.path.join(LOG_DIR, f"{module}.json")

    entry = {
        "time": str(datetime.now()),
        "module": module,
        "data": data
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
