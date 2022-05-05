for i in range(1,6):
    msg = f"{i} - building"
    print(msg.center(50,"-"))
    if i == 3:
        print("no")
        continue
    for j in range(1,10):
        print(f"live in {i}-{j}")
        if i == 4 and j ==4:
            print("you are died")
            break
        