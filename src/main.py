import student
import manager 

from Helpers.db import load_json, save_json, STUDENTS, MANAGERS
from Helpers.HashHelper import verify_pin

def menu():
        while True:
            db_students = load_json(STUDENTS)
            db_managers = load_json(MANAGERS)

            print("------INTERFACE------")
            print(f"""
                [1.] Student
                [2.] Manager
                [3.] Exit
                """)

            try:
                choice = int(input(""))
            except Exception as e:
                continue

            if choice == 1:
                if len(db_students) == 0:
                    print("No students. Cannot enter.")
                    continue

                student_id = str(input("Enter your student ID: "))
                if student_id in db_students:
                    student_pin = str(input("Enter your student pin: "))
                    auth = verify_pin(student_id, student_pin, STUDENTS)
                    if auth:
                        student.run(student_id)
                    else:
                        print("Incorrect pin.")
                        continue
                else:
                    print("Student does not exist.")
                    continue
            elif choice == 2:
                manager_id = str(input("Enter employee ID: ")) 
                if manager_id in db_managers:
                    manager_pin = str(input("Enter pin: "))
                    auth = verify_pin(manager_id, manager_pin, MANAGERS)
                    if auth:
                        manager.run(manager_id)
                    else:
                        print("Incorrect pin.")
                        continue
                else:
                    print("Manager does not exist.")
                    continue
            elif choice == 3:
                break
                exit()
            else:
                print("Option does not exist.")
                continue

menu()
