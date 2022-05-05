# alien_0 = {'color': 'green','points': 5,'speed':'medium'}
# # print(alien_0['color'])
# # print(alien_0['points'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# # print(alien_0)
# #
#
# # alien_0 = {}
# # alien_0['x_position'] = 0
# # alien_0['y_position'] = 25
# # alien_0['color'] = 'green'
# # alien_0['points'] = 5
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
#
# del alien_0['color']
# print(alien_0)
#

favorite_music ={
    'jen':'python',
    'ava':'c',
    'bella':'c++'
}

info = {
    'first_name':'Zheng',
    'last_name':'Zitao',
    'city':'WuXi'
}
# for key,value in info.items():
#     print('\nKey: '+key)
#     print('Value: '+value)
for key in info.keys():
    print(info[key])
for value in info.values():
    print(value)
lis = list(info.keys())
print(lis)