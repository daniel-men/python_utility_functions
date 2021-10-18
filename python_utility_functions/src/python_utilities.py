from datetime import datetime
import json

def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}

def create_timestamp() -> str:
    dt = datetime.now()
    return f"{dt.year}-{dt.month}-{dt.day}-{dt.hour}-{dt.minute}-{dt.second}"

def load_from_json(path: str) -> dict:
    with open(path, 'r') as f:
        return json.load(f)

def save_to_json(path: str, data) -> None:
    with open(path, 'w') as f:
        json.dump(data, f)