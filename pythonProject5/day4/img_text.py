# f = open("xjpic.jpg","rb")  #使用二进制进行读写 rb、wb
# for line in f:
#     print(line)

f = open("wb_file","wb")

s = "郑子涛"
# f.write(s.encode("gbk"))
f.write(s.encode("utf-8"))