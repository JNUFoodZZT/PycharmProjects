#
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('you cannot divied by zero!')

print("Give me two number and i'll divide them")
print("input q to quit\n")
while True:
    first_number = input("\n first number:")
    if first_number == 'q':
        break
    second_number = input("\n second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print('you cannot divied zero!')
    else:
        print(answer)
