import json
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "DataBase"

STUDENTS = DATA_DIR / "students.json"
HISTORY = DATA_DIR / "history.json"
VIOLATIONS = DATA_DIR / "violations.json"
MANAGERS = DATA_DIR / "managers.json"

def load_json(file_path):
    file_path = pathlib.Path(file_path)

    if not file_path.exists():
        if file_path.name in ["history.json", "violations.json"]:
            return []
        return {}
    
    with open(file_path, "r") as f:
        return json.load(f)

def save_json(file_path, data):
    file_path = pathlib.Path(file_path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    tmp_file = file_path.with_suffix(".tmp")

    with open(tmp_file, "w") as f:
        json.dump(data, f, indent=4)

    tmp_file.replace(file_path)
