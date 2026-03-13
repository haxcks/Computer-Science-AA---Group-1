import datetime

students = {
    "14-2024-007":{"name":"Jhustin","room":"210","status":"OUT","passkey":"1234"},
    "14-2024-013":{"name":"Jemdrich","room":"203","status":"OUT","passkey":"2345"},
    "14-2024-023":{"name":"Jakob","room":"212","status":"OUT","passkey":"3456"},
    "14-2024-015":{"name":"Liam","room":"211","status":"OUT","passkey":"4567"},
    "14-2024-006":{"name":"Ae-shin","room":"204","status":"OUT","passkey":"4567"}
    }

curfew = datetime.time(18,0)

history = []
violations = []

def student_menu(student_id):
    violation = False
    now = datetime.datetime.now()
    
    student = students[student_id]

    while True:
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

                print("Check-in time: " + now.strftime("%Y-%m-%d %H:%M"))

                if now.time() > curfew:
                    print("Late check-in!")
                    violations.append({
                        "id": student_id,
                        "viol": "Late Check-in",
                        "time": now.strftime("%Y-%m-%d %H:%M"),
                        })
                    violation = True

                history.append({
                    "id": student_id,
                    "status": "IN",
                    "time": now.strftime("%Y-%m-%d %H:%M"),
                    "violation": violation,
                    })
            case 2:
                if student["status"] == "OUT":
                    print("Cannot check-out if already checked-out!")
                    continue
                
                student["status"] = "OUT"

                history.append({
                    "id": student_id,
                    "status": "OUT",
                    "time": now.strftime("%Y-%m-%d %H:%M"),
                    "violation": violation,
                    })

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

                found = False

                for violation in violations:
                    if violation["id"] == student_id:
                        print(violation["viol"], "-", violation["time"])
                        found = True

                if not found:
                    print("No violations.")

            case 5:
                print("Logging Out...")
                break

def man_menu():

    while True:
        print("----- Manager Dashboard -----")
        print("1 : View Student Profiles")
        print("2 : View Violations")
        print("3 : View Student History")
        print("4 : Logout")

        try:
            choice = int(input("Choice: "))
        except ValueError as e:
            print("Invalid choice!")
            continue

        match choice:
            case 1:
                print("----- Student Profiles -----")

                for student_id in students:
                    student = students[student_id]

                    print("ID:", student_id)
                    print("Name:", student["name"])
                    print("Room:", student["room"])
                    print("Status:", student["status"])
                    print("-------------------")
            case 2:
                print("----- Violations -----")

                if len(violations) == 0:
                    print("No violations recorded.")
                    continue

                for violation in violations:
                    print("Student ID:", violation["id"])
                    print("Violation:", violation["viol"])
                    print("Time:", violation["time"])
                    print("-------------------")
            case 3:
                print("----- Student History -----")

                if len(history) == 0:
                    print("No history yet.")

                else:
                    for historie in history:
                        print("Student ID:", historie["id"])
                        print("Status:", historie["status"])
                        print("Time:", historie["time"])
                        print("-------------------")
            case 4:
                print("Logging out...")
                break

                    
def main():
    while True:

        print("----- DORMITORY SYSTEM -----")
        print("1 : Student")
        print("2 : Manager")
        print("3 : Exit")

        try:
            choice = int(input("Choice: "))
        except ValueError as e:
            print("Invalid Choice!")
            continue

        match choice:
            case 1:

                student_id = input("Student ID: ")

                if student_id not in students:
                    print("Student-id doesn't exist!")
                    continue
                
                passkey = input("Passkey: ")

                if students[student_id]["passkey"] != passkey:
                    print("Invalid login.")

                print("Login successful")
                student_menu(student_id)
                

            case 2:

                name = input("Manager Name: ")
                passkey = input("Manager Passkey: ")

                if name != "Bella" or passkey != "RHMANAGER":
                    print("Invalid login.")
                    continue
                    
                man_menu()
                    

            case 3:
                print("Thank you for using the program.")
                break

if __name__ == "__main__":
    main()
