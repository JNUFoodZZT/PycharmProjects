count = 0
while count < 4:
    count += 1
    grade = int(input("your grade is____(0-100)"))
    if grade >= 95:
        print("A")
        print(f"this is {count}")
        break
    elif grade >= 85:
        print("B")
    elif grade >= 75:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
    print(f"this is {count}")