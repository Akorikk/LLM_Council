import json
from datetime import datetime


def log_event(event_type: str, payload: dict):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "payload": payload
    }

    with open("audit_log.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")
