stu_list = [['ava',72],['bella',65],['carol',48],['dinna',95],['elien',92],['mark',68],['rose',87],['canna',69],['faker',97],['rookie',88],['doina',60],['doinb',67],['doinc',80]]
new_stu_list = [[],[],[],[],[]]
# for n in range(12):
#     m = stu_list[n][-1]
#     if  m >= 90:
#         new_stu_list[0].insert(0,stu_list[n])
#     elif m >= 80:
#         new_stu_list[1].insert(0,stu_list[n])
#     elif m >= 70:
#         new_stu_list[2].insert(0,stu_list[n])
#     elif m >= 60:
#         new_stu_list[3].insert(0,stu_list[n])
#     else:
#         new_stu_list[4].insert(0,stu_list[n])
# print(new_stu_list)

for i in stu_list:
    if i[1] >=90:
        new_stu_list[0].append(i)
    elif i[1] >= 80:
        new_stu_list[1].append(i)
    elif i[1] >= 70:
        new_stu_list[2].append(i)
    elif i[1] >= 60:
        new_stu_list[3].append(i)
    else:
        new_stu_list[4].append(i)
print(new_stu_list)