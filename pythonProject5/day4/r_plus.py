# f = open("1","r+")
# print(f.readline(2))
# print(f.tell())
# f.seek(f.tell())
# f.write(" new one \n")

# f = open("1","r+")
# # 加载内存
# data = f.read()
# old_str_count = data.count("1")
# print(f"the times is {old_str_count}, {data}")
# new_data = data.replace("1","2")
# # 清除内容
# f.seek(0)
# f.truncate()# 截断文件
# # 写入硬盘
# f.write(new_data)
# f.close()

test1 = open("1", "r")

t = test1.split()

print(f"{t},{len(t)}")
