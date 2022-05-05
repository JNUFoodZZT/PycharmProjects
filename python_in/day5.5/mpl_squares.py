import matplotlib.pyplot as plt
from random_walk import RandomWalk

# input_value = list(range(1,5001))
# squares = [x**3 for x in input_value]
# # plt.plot(input_value,squares,linewidth=4)
# #设置图标标题 坐标标签
# plt.title("square number",fontsize=24)
# plt.xlabel("value",fontsize=14)
# plt.ylabel("square",fontsize=14)
# #刻度大小
# plt.tick_params(axis='both',which='major',size=3)
#
#
# plt.scatter(input_value,squares,c=squares,cmap=plt.cm.Blues,edgecolors='none',s=10)
#
#
#
# plt.show()


rw = RandomWalk(5000)
rw.walk()

plt.figure(dpi=128,figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,
            c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=5)
plt.plot(rw.x_values,rw.y_values,linewidth=0.1)
plt.scatter(0,0,c='red',edgecolors='none',s=10)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
plt.show()

