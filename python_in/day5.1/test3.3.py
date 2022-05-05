wifes= ['ava','bella','carol','dianna','elieen']
print(wifes)
cannot = 'bella'
wifes.remove('bella')
print('sorry and '+ cannot +' cannot go on')
wifes.insert(1,'kire')
print(wifes)
new_wifes = ['qihai','gonghai','lkd']
for i in range(len(new_wifes)):
    wifes.append(new_wifes[i])
print(wifes)
wifes.insert(0,'dad')
print(wifes)


print('sorry for you that i can just invite two people')
for i in range(len(wifes)):
    if len(wifes) > 2:
        sor = wifes.pop()
        print('sorry for you '+ sor)
    else:
        fine = wifes[-1]
        print('you win '+ fine)
        del wifes[-1]
print(wifes)