#闰年判断
while 1:
    temp=input('请输入年份：')
    while not temp.isdigit():    # .isdigit()为字符串内置方法,判断是否只包含数字, 返回布尔值
        temp=input('请输入整数年份：')
    year=int(temp)
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        print(temp + '年是闰年')
    else:
        print(temp + '年不是闰年')
        print('')
