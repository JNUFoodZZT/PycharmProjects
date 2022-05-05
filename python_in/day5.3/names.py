from function_test import get_name

print("enter 'q' to quit at any time")
while True:
    first = input('your first name:')
    if first == 'q':
        break
    last = input('your last name:')
    if last == 'q':
        break
    fullname = get_name(first,last)
    print(f"your full name is {fullname}")