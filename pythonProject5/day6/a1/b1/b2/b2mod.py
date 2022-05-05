import os
import sys
import datetime
# from day6.a1.a2 import a2mod
d = datetime.datetime.now()
print(d + datetime.timedelta(5,hours=5)) # 时间运算
print(d.replace(year= 2000,month=8,day=25))