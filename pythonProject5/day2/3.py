sym = "*"

for j in range(1,10):
    if j <= 5:
        print(j * sym)
    else:
        for i in range(2,6):
            print((j - i) * sym)
        break



