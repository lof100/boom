#输入圆的半径计算周长和面积

import math

r=float(input('请输入圆的半径：'))
p=math.pi*r*2
a=math.pi*r**2

print('圆的周长为%.2f' %p)
print('圆的面积为%.2f' %a)
