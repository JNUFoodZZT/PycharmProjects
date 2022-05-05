

def count_words(filename):
    """计算txt文件中字符数"""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(' not found')
        # pass
    else:
        words = contents.split()
        new_words = len(words)
        print(f"the number of <{filename}> is {new_words} ")


filenames = ['lover.txt','heating.txt']
for filename in filenames:
    count_words(filename)