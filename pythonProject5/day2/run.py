import random
import string
for m in range(3):
    car_num = []
    for i in range(20):
        a = ["A","B","C","D","E"]
        s = string.ascii_uppercase + string.digits
        n = random.sample(s,5)
        k = "".join(n)
        c_num = f"京{random.choice(a)}-" + k
        car_num.append(c_num)
        print(f"the {i+1}st is  {c_num}")
    choice = input("你的选择是").strip()
    if choice in car_num:
        print(f"ok,it's  {choice}")
        break
    else:
        print("--------------------------")
        print(f"maybe, you don't like these,you have {2-m} times,return")
        if m == 2:
            print("sorry")
