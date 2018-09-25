#-*- encoding:utf-8 -*-
print(123)

a=1123
b=234
print(a+b)

age1=50
age2=age1
age3=age2
age2=100
print(age1,age2,age3)

print("我是帅哥")

print('帅哥'*3)
msg="""
一二三四五
上山打老虎
老虎没打到
打只小松鼠
"""
print(msg)
print(True,type(True))
'''
name=input('请输入你的名字')
age=input('请输入你的年龄')
print('我的名字是：'+name+'，我的年龄'+age+'岁')
'''

if 4>5:
    print('我请你吃翔')

if 4>5:
    print("我请你吃翔")
elif 5>4:
    print("我请你喝酒")
else :
    print("我请你喝酒")

score=int(input("输入分数："))

if score>100:
    print("牛逼，超出天际")
elif score>=90:
    print("给A")
elif score>=60:
    print("给C")
elif score>=80:
    print("给B")
elif score>=40:
    print("给D")
else :
    print("脑残给E")