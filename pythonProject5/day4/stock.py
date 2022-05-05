def stock(arg = None,height = None,weight = None):
    info = {} # dict
    f = open("stock_data","r")
    for line in f:
        line = line.strip().split()
        info[line[0]] = line

    if arg in info:
        print(info[arg])
    else:
        print("sorry none")
    print(info)
    # for i in range(len(info)):
    #     if height == info[1]:
    #         print()

stock(arg= "ava")