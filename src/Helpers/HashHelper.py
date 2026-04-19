import hashlib
from Helpers.db import load_json, STUDENTS 


def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()

def verify_pin(id, pin, db) -> bool:
    datebase = load_json(db)

    if id not in datebase:
        return False

    stored_hash = datebase[id]["pin_hash"]
    return stored_hash == hash_pin(pin)

