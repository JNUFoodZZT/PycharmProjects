i = 0
while i < 9:
    i += 1
    for j in range(1,i+1):
        if j==2 and (i==3 or i==4):
            print(f"{j}*{i}={j * i}", end="     ")
        else:
            print(f"{j}*{i}={j*i}",end="    ")
    print()





