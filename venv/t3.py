'''
i=100
print(i.bit_length()) #二进制

i =1
s=str(i)
print(s,type(s))
s1='12345'
i1=int(s1)
print(i1,type(i1))
'''
#int ----->bool  只要是0 ----》False  非0就是True
'''
i=3
b=bool(i)
print(b)
'''

'''
while True:
    pass
while 1:  #效率高
    pass
'''
#非空字符串都是True
#s = "0" -----> True
s="0"

if s:
    print(1)
else:
    print(0)