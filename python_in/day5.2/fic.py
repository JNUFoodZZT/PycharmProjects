# def show_wifes(list):
#     for wife in list:
#         print(wife)
#
# wifes =['ava','bella','carol','diana','elieen']
#
#
# def make_great(list):
#     great_list = []
#     while list:
#         great_list.append(f'great {list.pop()}')
#     show_wifes(great_list)
#
# print(wifes)
# show_wifes(wifes)
# make_great(wifes[:])

# def make_pizza(*args):
#     for topping in args:
#         print(f"i'll add {topping} in yours")
#     print('that is all')
#
# make_pizza('ava')
# make_pizza('ava','bella','carol')

def profile(first,last,**kwargs):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in kwargs.items():
        profile[key] = value
    return profile

mesg = profile('zheng','zitao',location= 'wuxi',age= '22')
print(mesg)