# message= input('tell me what you want ')
# print(message)
#
# age = input("what's your age: ")
# print(int(age))

message = 'tell me what you want yo add in your pizza'
message += "\nand input quit when it's over"
message += "\nyou want:"
toppings = []
while True:
    addition = input(message)
    if addition != 'quit':
        toppings.append(addition)
        print(f"ok, i will add {addition}")
    else:
        print(f"all you want is {toppings}")
        break