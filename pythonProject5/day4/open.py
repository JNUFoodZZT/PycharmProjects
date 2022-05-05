# # f = open("name_list","r") # mode r 只读模式 w 创建模式；a 追加模式; # r+ w+ a+...
# # f.write("wu hu da si\n")
# # f.write("ma\n")
# # f.close()
# f = open("name_list","r")
# # print(f.read())
# print(f.readline())

f = open("1")
for line in f:#每循环一次读一行
    line = line.split()
    # print(line),注意回车、空格问题
    height = int(line[3])
    weight = int(line[4])
    if height >= 160 and weight <= 50:
        # print("----------")
        print(line)