# def load(account, password):
#     info = open("infomation","w")
#     info.write(f"{account} {password}")
#     info.close()
#     print("load successfully!")
#     return

def test():
    test1 = open("infomation", "r+")
    for line in test1:  # 每循环一次读一行
        line = line.split()
        print(line)
        for n in range(4):
            if n< 3:
                print("your account is: ")
                account = input()
                print("your password is: ")
                password = input()
                if str(account) == line[0] and str(password) == line[1]:
                    print("pass!")
                    exit()
                else:
                    print("wrong!")
            else:
                print("locked!")


# load("jiack12","123qwe")

# def test():
#     test1 = open("infomation", "r+")


test()

