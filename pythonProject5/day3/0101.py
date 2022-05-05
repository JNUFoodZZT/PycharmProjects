stu_list = [
    ['ava', 72, 0], ['bella', 65, 0], ['carol', 48, 0], ['dinna', 95, 0], ['elien', 92, 0],
    ['mark', 68, 1], ['rose', 87, 1], ['canna', 69, 1], ['faker', 97, 1], ['rookie', 88, 1],
    ['doina', 60, 1], ['doinb', 67, 1], ['doinc', 80, 0], ['ded', 19, 1], ['mom', 42, 0], ['dad', 4, 1]
]
info = {
    9: [],
    8: [],
    7: [],
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: [],
    0: []
}
for i in stu_list:
    for m in range(10):
        if m* 10 <= i[1] < (m+ 1)* 10:
            info[m].append(i)
print(info)
    # if i[1] < 10:
    #     info[0].append(i)
    # elif 10 <= i[1] <20:
    #     info[1].append(i)
    # elif