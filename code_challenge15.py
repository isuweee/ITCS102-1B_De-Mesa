import os

os.system('cls')
print("======================================")
print("===== STUDENT INFORMATION SYSTEM =====")
print("======================================\n")

record = {}
while True:
    print("===== OPTIONS =====")
    print("A = Add student record.")
    print("B = Print all student record.")
    print("C = Search student record.")
    print("D = Delete student record.")
    print("E = Edit student record.")
    print("F = Export student record.")
    print("G = Exit.")
    print("====================\n")

    pick = input("SELECT OPTION FROM ABOVE: ").lower()

    if pick == 'a':
        print("\n=== ADDING STUDENT RECORD ===\n")
        id = input("Student ID: ").upper()
        fn = input("First Name: ").upper()
        ln = input("Last Name: ").upper()
        age = eval(input("Age: "))
        section = input("Section: ").upper()
        course = input("Course: ").upper()

        record[id] = [fn, ln, age, section, course]
        print("\n======== DATA SAVED ========\n")

        continue
    elif pick == 'b':
        print("===== STUDENT RECORD =====")
        for a, d in record.items():
            print(f'CODE - {a}, INFORMATION - {d}')
        continue
    elif pick == 'c':
        pass
        continue
    elif pick == 'd':
        pass
        continue
    elif pick == 'e':
        pass
        continue
    elif pick == 'f':
        pass
        continue
    elif pick == 'g':
        print("SYSTEM EXIT")
        break
    else:
        print("Invalid Choice")
