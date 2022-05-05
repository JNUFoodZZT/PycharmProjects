import random
import string
count = []
count2 = []
a, i, n = 1, 0, 0

for j in range(300):
    j += 1
    count.append(j)
print(f"please enter ok to star the 3 reword!  :  ")
{input()}
while i in range(30):
    three = random.randint(1,300)
    i += 1
    if three not in count2:
        print(i,three,"good luck!")
        count2.append(three)
    else:
        i -= 1
print(f"please enter ok to star the 2 reword!  :  ")
{input()}
while n in range(3):
    two = random.randint(1,300)
    n += 1
    if two not in count2:
        print(n,two,"good luck!")
        count2.append(two)
    else:
        n -= 1
print(f"please enter ok to star the 1 reword!  :  ")
{input()}
while a :
    one = random.randint(1,300)
    if one not in count2:
        print(one,"goodgood luck!")
        count2.append(one)
        a = 0
print("\n\n\n\nthat's all",count2)

