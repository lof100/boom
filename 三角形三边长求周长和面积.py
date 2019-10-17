#三角形三边长求周长和面积
while 1:
    a=float(input('请输入a边长:'))
    b=float(input('请输入b边长:'))
    c=float(input('请输入c边长:'))
    if a+b>c and a+c>b and b+c>a:
        print('三角形周长为',(a+b+c))
        p=(a+b+c)/2
        area=(p*(p-a)*(p-b)*(p-c))**0.5
        print('三角形面积为',area)
    else:
        print('三条边不能构成三角形')
