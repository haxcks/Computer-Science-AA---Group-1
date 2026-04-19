import json
import os

from datetime import datetime, time

from Helpers.db import load_json, save_json, HISTORY, VIOLATIONS, STUDENTS
from Helpers.HashHelper import verify_pin, hash_pin
from API.TimeAPI import getTime

def log_history(student_id, vbool, status):
    history = load_json(HISTORY)

    dt = getTime()

    history.append({
        "student_id": student_id,
        "status": status,
        "violation": vbool,
        "timestamp": dt.isoformat(),
        "formatted": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": getattr(dt.tzinfo, "key", str(dt.tzinfo))
    })

    save_json(HISTORY, history)

def log_violation(student_id, vtype, note=""):
    violations = load_json(VIOLATIONS)

    dt = getTime()

    violations.append({
        "student_id": student_id,
        "type": vtype,
        "timestamp": dt.isoformat(),
        "formatted": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": getattr(dt.tzinfo, "key", str(dt.tzinfo)),
        "note": note
    })

    save_json(VIOLATIONS, violations)
    
def main(student_id):
    db_students = load_json(STUDENTS)
    db_log = load_json(HISTORY)
    db_violations = load_json(VIOLATIONS)

    violation = False
    now = getTime()
    
    curfew = time(18, 0)

    student = db_students[student_id]

    while True:    
        db_students = load_json(STUDENTS)
        db_log = load_json(HISTORY)
        db_violations = load_json(VIOLATIONS)
        
        print("""
----- Student Dashboard -----
1 : Check-in
2 : Check-out
3 : View Student Profile
4 : View Student Violations
5 : Logout
""")
        try:
            choice = int(input("Choice: "))
        except ValueError as e:
            print("\nNot a choice!")
            continue

        if choice not in [1,2,3,4,5]:
            print("\nNot a choice!")
            continue

        match choice:
            case 1:
                if student["status"] == "IN":
                    print("Cannot check-in if already checked-in!")
                    continue
                
                student["status"] = "IN"
                save_json(STUDENTS, db_students)

                print("Check-in time: " + now.strftime("%Y-%m-%d %H:%M"))

                if now.time() > curfew:
                    print("Late check-in!")
                    log_violation(student_id, "Late Check-in", "Created by SYSTEM")
                    violation = True

                log_history(student_id, violation, "IN")
            case 2:
                if student["status"] == "OUT":
                    print("Cannot check-out if already checked-out!")
                    continue

                student["status"] = "OUT"
                save_json(STUDENTS, db_students)

                log_history(student_id, violation, "OUT")

                print("Check-out time: " + now.strftime("%Y-%m-%d %H:%M"))
            case 3:
                print(f"""
---- Profile ----
Name: {student["name"]}
Room: {student["room"]}
Status: {student["status"]}
""")
            case 4:
                print("----- Your Violations -----")

                if len(db_violations) == 0:
                    print("No violations.")
                    continue

                for violation in db_violations:
                    if violation["student_id"] == student_id:
                        print(f"Student ID: {student_id}")
                        print(f"Violation Type: {violation["type"]}")
                        print(f"Formatted Time: {violation["formatted"]}")
                        print(f"Note: {violation["note"]}\n")

            case 5:
                print("Logging Out...")
                break


def run(student_id):
    main(student_id)
