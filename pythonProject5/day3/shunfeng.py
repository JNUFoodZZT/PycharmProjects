# string


a = ["alex li line"]
b = ["alex","box","caral","ava","dinna","box"]

# print(a.count("l",0,4))
# print(a.endswith("e"))
# print(a.startswith("al"))
# print(a.find("li"),a.find("ln"))     #返回 -1 代表没找到
# print(a.isdigit(),"22".isdigit())   #是否为int
# print("-".join(b)) #拼接
# print(a.replace("l","M",2))
# print(a.split("l"))     #按照空格分离字符串，输出list


#list [ , , , ]
# list 切片 a[3:5]顾头不顾尾
# b.insert(2,"ok")
# print(b[2])
# print("box" in b)
# print(b.index("box"))
# print(b.count("box"))
# b.pop() #默认删除最后一个值并返回，可指定
# b.remove("ava")#删除指定元素
# print(b)
# b.sort() 排序
# b.reverse() #反转
for i in enumerate(b):
    print(i[0],i[1])
