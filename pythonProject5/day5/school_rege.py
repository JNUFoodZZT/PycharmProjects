course_list = ["python", "linux", "html", "css", "java"]

def reg(name, age, tel, id, course):
    f = open("info", "r+")
    for n in f:
        a = n.strip().split()
        for k in a:
            if str(tel) == k:
                print("tel is regi")
                return
        for m in a:
            if str(id) == m:
                print("id is regi")
                return
    if course not in course_list:
        print("wrong course")
        return
    f.write(f"{name} ")
    f.write(f"{age} ")
    f.write(f"{tel} ")
    f.write(f"{id} ")
    f.write(f"{course}\n")
    f.close()
    print("successfully!")
    return

def use():
    name = input("your name is:")
    age = input("your age is:")
    tel = input("your tel is:")
    id = input("your id is:")
    print(f"we have these course: {course_list}")
    course = input("your course is:")
    reg(name, age, tel, id, course)

use()
