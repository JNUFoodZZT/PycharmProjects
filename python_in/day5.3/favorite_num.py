import json


# filename = 'favo_num.json'
# try:
#     with open(filename) as f_obj:
#         favo_num = f_obj.read()
# except FileNotFoundError:
#     favo_num = input('tell me your favorite number, i will remember it forever. ')
#     with open(filename,'w') as f_obj:
#         json.dump(favo_num,f_obj)
#         print('get it!')
# else:
#     print(f"yeah i know, your favorite number is {favo_num}!")

def get_favo_num():
    filename = 'favo_num.json'
    try:
        with open(filename) as f_obj:
            favo_num = f_obj.read()
    except FileNotFoundError:
        return None
    else:
        return favo_num

def new_favo_num():
    favo_num = input('tell me your favorite number, i will remember it forever. ')
    filename = 'favo_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(favo_num, f_obj)
        print('get it!')

def favo_num():
    favo_num = get_favo_num()
    if favo_num:
        print(f"yeah i know, your favorite number is {favo_num}!")
    else:
        new_favo_num()

favo_num()