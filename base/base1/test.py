print ("hello world!")
'''
你好
'''
b=11
c=11
print(b==c)
import keyword
print(keyword.kwlist)
if True:
    print ('你是个lv ', end='')
    print('点心！什么点心？')  # 缩进不一致运行会报错
else:
    print ("你才是")
#uname = input('请输入你的名字')
#print(uname)

a,b,c,d=1,2,3,4
print(a,b,c,d)
print('a=',id(a),' b=',id(b),' c=',id(c),' d=',id(d))
a,b,c,d=d,c,b,a
print(a,b,c,d)
print(type(a))
print('a=',id(a),' b=',id(b),' c=',id(c),' d=',id(d))
a=0b101011
print(0)
b=0o12370
print(b)
c=190
print(c)
d=0xabcdef
print(d)
f1=1.222
print(f1)
f2=1.22e-3
print(f2)
plural=1+4j
print(plural)
true=True
false=False
print(true)
print(false)
many='''cccc ccccc'''
print(many)
#列表 允许重复[]
list1=[222,33,"222","3333",3.123,3e10]
list1[0]=33
print(list1)
#元组 不能改变()
tuple=(12,3,3,4)
print(tuple)
#字典 HashMap{}
dic={'a':1,b:3}
print(dic)
#集合 set{}
set1={1,3,4}
print(set1)
var1='123'
var2=11
#字符串强制转换成int函数
print(int(var1)+var2)
#float函数转换成float型
print(float(var1)+var2)
print(3==False)
#bool函数
print(bool(4+5j))
#complex函数
print(complex(1+5j)==complex(1,5))
print(complex(1,5))
#str函数 变成字符串
print(str(list1))
#list函数变成列表类型
print(list(tuple))
print(list('123abcdef'))
print(list(list1))
print(list(dic))
set2={('aa','AA'),('bb','BB'),('cc','CC')}
list2=[('aa','AA'),('bb','BB'),('cc','CC')]
tuple1=(('aa','AA'),('bb','BB'),('cc','CC'))
#dict函数
print(dict(set2))
print(dict(list2))
print(dict(tuple1))
#set函数
tuple1=(12,3,4)
print(set(tuple1))
print(set('123abcdef'))
print(set(list1))
print(set(dic))
