'''
count=0
while count<=5:
    count+=1
    if count == 10:
        break
    print('loop',count)
else:
    print("正常循环完毕")
'''
#and or not
#优先级 ()>not>and>or
#print(2>1 and 1<4)  #True
#print(2>1 and 1>4)  #False
#print(2>1 and 5>4 or 4<3 and 9<6 or 1>4 and 3>2) #直接按照优先级来

'''
print(bool(2))
print(bool(0))
print(bool(-2))

print(int(True))
print(int(False))
'''
'''
print(1 or 2)  # 1
print(3 or 2)  # 3
print(0 or 2)  # 2
print(0 or 100)  # 100

print(2 and 100 and 3 or 4)
'''
'''
print(1 and 2)

print (2 or 1 <3)

print (3 > 1 or 4 and 3)
'''

#格式化输出,数量必须保持一致
# % s d
"""
name=input('请输入姓名：')
age=input('请输入年龄：')
height=input('请输入身高：')
msg="我叫%s，今年%s，身高%s" %(name,age,height)
print(msg)
"""
"""
name = input('请输入姓名:')
age = input('请输入年龄:')
job = input('请输入工作:')
hobbie = input('你的爱好:')

msg = '''------------ info of %s -----------
Name  : %s
Age   : %d
job   : %s
Hobbie: %s
------------- end -----------------''' %(name,name,int(age),job,hobbie)
print(msg)
"""

name = input('请输入姓名')
age = input('请输入年龄')
height = input('请输入身高')
msg = "我叫%s，今年%s 身高 %s 学习进度为3%%" %(name,age,height)
print(msg)

