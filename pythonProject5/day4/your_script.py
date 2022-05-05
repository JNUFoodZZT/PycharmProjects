def re(old_str,new_str,filename):
    f = open(filename,"r+")
    data = f.read()
    old_str_count = data.count(old_str)
    print(f"the times is {old_str_count}, {data}")
    new_data = data.replace(old_str, new_str)
    # 清除内容
    f.seek(0)
    f.truncate()  # 截断文件
    # 写入硬盘
    f.write(new_data)
    f.close()
    return
print(f"-----")
re("1","2","1")

# import sys
#
# print(sys.argv)
# old_str = sys.argv[1]
# new_str = sys.argv[2]
# filename = sys.argv[3]
# f = open(filename,"a+")
# data = f.read()
# old_str_count = data.count(old_str)
# new_data = data.replace(old_str, new_str)
# f.seek(0)
# f.truncate()
# f.write(new_data)
# f.close()
# print(f"the times is {old_str_count}")
