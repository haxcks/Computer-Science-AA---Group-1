"""
TimeAPI
Author: Haxs / Jakob Pabico
Version: 1.2
Description: Cross-language portable timezone API
"""


from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import pathlib
import json
import os

TIMEZONE_FILE = pathlib.Path(__file__).parent / "time.timeapi"
FALLBACK_TIMEZONE = "UTC"

def create_json(dt):
    tz = dt.tzinfo.key
    response = {
            "iso": dt.isoformat(),
            "timestamp": dt.timestamp(),
            "formatted": dt.strftime("%m-%d-%Y %H:%M:%S"),
            "timezone": tz,
            "year": dt.year,
            "month": dt.month,
            "day": dt.day,
            "dayOfWeek": dt.strftime("%A"),
            "hour": dt.hour,
            "minute": dt.minute,
            "second": dt.second
    }
    json_str = json.dumps(response, indent=4)

    tmp_file = "TimeAPIJson.tmp"
    json_file = "TimeAPIJSON.json"

    with open(tmp_file, "w") as f:
        f.write(json_str)
    os.replace(tmp_file, json_file)

    return json_str

def getTime(override: str | None = None, save_json: bool = False) -> str | datetime:
    timezone_str = None

    if override:
        timezone_str = override.strip()
    else:
        try:
            timezone_str = TIMEZONE_FILE.read_text().strip()
        except FileNotFoundError:
            print(f"Error: FileNotFound\nDefaulting to {FALLBACK_TIMEZONE}")
            timezone_str = FALLBACK_TIMEZONE

    try:
        timezone = ZoneInfo(str(timezone_str).strip())
    except ZoneInfoNotFoundError:
        timezone = ZoneInfo(FALLBACK_TIMEZONE)
    
    timezone_now = datetime.now(timezone)

    if save_json:
        create_json(timezone_now)


    return timezone_now

