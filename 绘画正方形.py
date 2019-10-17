import turtle

'''
一个简单的绘图工具，叫做海龟绘图(Turtle Graphics)
turtle库是python的内部库
'''


turtle.pensize(5)   #turtle.pensize()：设置画笔的宽度
turtle.pencolor('red')

'''
没有参数传入,返回当前画笔颜色,
传入参数设置画笔颜色
可以是字符串如"green", "red",也可以是RGB 3元组
'''

turtle.forward(100)  #向当前画笔方向移动distance像素长
turtle.right(90)     #顺时针移动degree°
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
'''
turtle.mainloop()或turtle.done()

启动事件循环 -调用Tkinter的mainloop函数。

必须是乌龟图形程序中的最后一个语句。
'''
