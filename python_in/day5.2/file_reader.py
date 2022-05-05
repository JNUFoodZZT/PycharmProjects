
# filename = 'pi.txt'
# with open(filename) as file_object:
#     # contents = file_object.read()
#     # print(contents)
#
#     # for line in file_object:
#     #     print(line.rstrip())
#     # contents = file_object.read()
#     # print(contents)
#     #
#     # for line1 in file_object:
#     #     print(line1)
#
#     lines = file_object.readlines()
# for line in lines:
#     line.replace('python','C')
#     print(line)

filename = 'programming.txt'
with open(filename,'a+') as file:
    while True:
        name = input('your name(and input q to quit!):')
        if name == 'q':
            print('it is over')
            break
        file.write(f"{name}\n")