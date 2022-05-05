
stu_list = [['ava',72,0],['bella',65,0],['carol',48,0],['dinna',95,0],['elien',92,0],['mark',68,1],['rose',87,1],['canna',69,1],['faker',97,1],['rookie',88,1],['doina',60,1],['doinb',67,1],['doinc',80,0]]
# dic{
#     key1: value1,
#     key2:value2
# }
# key 唯一且不可变，value为任意
info = {
    'ava': ['ava',72,0],
    "bella": ['bella',65,0],
    'carol': ['carol',48,0],
    'dinna': ['dinna',95,0],
    'elien':['elien',92,0],
    'mark': ['mark',68,1],
    'rose': ['rose',87,1],
    'canna': ['canna',69,1],
    'faker': ['faker',97,1],
    'rookie': ['rookie',88,1],
    'doina': ['doina',60,1],
    'doinb': ['doinb',67,1],
    'doinc': ['doinc',80,0]
}
print('mark' in info) #查key
print(info['bella'])
# info["zheng"]=['zheng',89,1] 增加、修改dic
# del info['canna']
# info.pop('doinb') 两种删除
print(info)
for k in info.keys():
    print(k)
for k in info.values():
    print(k)
for k in info.items():
    print(k)
# for k,v in info.items(): #for 循环可以多变量
#     print(k,v)
for k in info:
    print(k,info[k])
# 可嵌套