from API.TimeAPI import getTime
from Helpers.db import load_json, save_json, VIOLATIONS, STUDENTS, HISTORY, MANAGERS
from Helpers.HashHelper import hash_pin

def add_violation(student_id, manager_id, vtype, note=""):
    db_violations = load_json(VIOLATIONS)
    db_history = load_json(HISTORY)
    db_students = load_json(STUDENTS)

    dt = getTime()

    if note == "":
        note = "NONE - Created by SYSTEM"

        db_violations.append({
            "student_id": student_id,
            "type": vtype,
            "timestamp": dt.isoformat(),
            "formatted": getattr(dt.tzinfo, "key", str(dt.tzinfo)),
            "note": note
            })        

    else:
        db_violations.append({
            "student_id": student_id,
            "type": vtype,
            "timestamp": dt.isoformat(),
            "formatted": getattr(dt.tzinfo, "key", str(dt.tzinfo)),
            "note": note + " - Created by " + manager_id 
            })

    db_history.append({
        "student_id": student_id,
        "status": db_students[student_id]["status"],
        "violation": True,
        "timestamp": dt.isoformat(),
        "formatted": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": getattr(dt.tzinfo, "key", str(dt.tzinfo))
        })

    save_json(VIOLATIONS, db_violations)
    save_json(HISTORY, db_history)

def add_student(student_id, name, room, pin):
    students = load_json(STUDENTS)

    if student_id in students:
        print("Student already exists.")
        return

    students[student_id] = {
            "name": name,
            "pin_hash": hash_pin(pin),
            "room": room,
            "status": "OUT"
    }

    save_json(STUDENTS, students)
    print("Student added.")

def remove_student(student_id):
    students = load_json(STUDENTS)

    if student_id in students:
        del students[student_id]
        print("Student removed.")
        save_json(STUDENTS, students)
        return
    
    print("Student does not exist.")
    return

def add_manager(manager_id, name, pin):
    managers = load_json(MANAGERS)

    if manager_id in managers:
        print("Manager already exists.")
        return

    managers[manager_id] = {
            "name": name,
            "pin_hash": hash_pin(pin)
        }
    
    save_json(MANAGERS, managers)
    print("Manager added.")

def remove_manager(manager_id):
    managers = load_json(MANAGERS)

    if manager_id == "SYSTEM":
        print(f"Manager {manager_id} CANNOT be removed.")
        return

    if manager_id in managers:
        del managers[manager_id]
        print("Manager removed.")
        save_json(MANAGERS, managers)
        return
    
    print("Manager does not exist.")
    return

def list_students():
    students = load_json(STUDENTS)
    
    for student_id, student_values in students.items():
        print(f"Student ID: {student_id}")
        for key, value in student_values.items():
            print(f" - {key}:{value}")

def man_menu(manager_id):
    while True:
        db_students = load_json(STUDENTS)
        db_violations = load_json(VIOLATIONS)
        db_history = load_json(HISTORY)
        db_managers = load_json(MANAGERS)

        print("----- Manager Dashboard -----")
        print("1 : Student Manage")
        print("2 : Manager Manage")
        print("3 : History & Violations")
        print("4 : Logout")

        try:
            choice = int(input("Choice: "))
        except ValueError as e:
            print("Invalid choice!")
            continue
        
        match choice:
            case 1:
                while True:                
                    db_students = load_json(STUDENTS)
                    db_violations = load_json(VIOLATIONS)
                    db_history = load_json(HISTORY)
                    db_managers = load_json(MANAGERS)

                    print("1 : Add Student")
                    print("2 : Remove Student")
                    print("3 : View Student Profiles")
                    print("4 : Exit")

                    try:
                        sub_choice = int(input(""))
                    except ValueError as e:
                        print("Invalid choice!")
                        continue
                    
                    match sub_choice:
                        case 1:
                            print("----- Add Student -----")
                            student_id = str(input("Enter student id: "))
                            name = str(input("Enter student name: "))
                            room = str(input("Enter student room: "))
                            pin = str(input("Enter student pin: "))

                            add_student(student_id, name, room, pin)
                        case 2:
                            print("---- Remove Student -----")
                            student_id = str(input("Enter student id: "))

                            remove_student(student_id)
                        case 3:
                            print("----- Student Profiles -----")

                            for student_id in db_students:
                                print("ID:", student_id)
                                print("Name:", db_students[student_id]["name"])
                                print("Room:", db_students[student_id]["room"])
                                print("Status:", db_students[student_id]["status"])
                                print("-------------------")
                        case 4:
                            print("Exiting...")
                            break
                    
            case 2:
                while True:                
                    db_students = load_json(STUDENTS)
                    db_violations = load_json(VIOLATIONS)
                    db_history = load_json(HISTORY)
                    db_managers = load_json(MANAGERS)

                    print("1 : Add Manager")
                    print("2 : Remove Manager")
                    print("3 : Exit")

                    try:
                        sub_choice = int(input(""))
                    except ValueError as e:
                        print("Invalid choice!")
                        continue

                    match sub_choice:
                        case 1:
                            print("----- Add Manager -----")
                            manager_id = str(input("Enter manager id: "))
                            manager_name = str(input("Enter manager name: "))
                            manager_pin = str(input("Enter manager pin: "))

                            add_manager(manager_id, manager_name, manager_pin)
                            print("-----------------------")
                        case 2:
                            print("----- Remove Manager -----")
                            manager_id = str(input("Enter manager id: "))

                            remove_manager(manager_id)
                            print("-----------------------------")
                        case 3:
                            print("Exiting...")
                            break
            case 3:
                while True:                
                    db_students = load_json(STUDENTS)
                    db_violations = load_json(VIOLATIONS)
                    db_history = load_json(HISTORY)
                    db_managers = load_json(MANAGERS)

                    print("1 : Add Violation")
                    print("2 : View Violations")
                    print("3 : View History")
                    print("4 : Exit")

                    try:
                        sub_choice = int(input(""))
                    except ValueError as e:
                        print("Invalid choice!")
                        continue

                    match sub_choice:
                        case 1:
                            print("----- Add Violation -----")
                            student_id = str(input("Enter student id: "))
                            vtype = str(input("Enter violation: "))
                            note = str(input("Enter note: "))

                            add_violation(student_id, manager_id, vtype, note)
                        case 2:
                            print("----- Violations -----")

                            if len(db_violations) == 0:
                                print("No violations recorded.")
                                continue

                            for violation in db_violations:
                                print("Student ID:", violation["student_id"])
                                print("Violation:", violation["type"])
                                print("Timestamp:", violation["timestamp"])
                                print("Formatted Time:", violation["formatted"])
                                if len(violation["note"]) == 0:
                                    print("Note: NONE")
                                else:
                                    print("Note:", violation["note"])
                                print("-------------------")
                        case 3:
                            print("----- Student History -----")

                            if len(db_history) == 0:
                                print("No history yet.")

                            else:
                                for history in db_history:
                                    print("Student ID:", history["student_id"])
                                    print("Status:", history["status"])
                                    print("Violation:", history["violation"])
                                    print("Timestamp:", history["timestamp"])
                                    print("Formatted Time:", history["formatted"])
                                    print("Timezone:", history["timezone"])
                                    print("-------------------")
                        case 4:
                            print("Exiting...")
                            break
            case 4:
                print("Logging out...")
                break


def run(manager_id):
    man_menu(manager_id)

