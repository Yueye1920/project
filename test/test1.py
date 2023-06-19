# print("hello world");

# text='ABCDEF'
# print(text)
# print(text[0:-1])
# print(text[0])
# print(text[2:5])
# print(text[2:])
# print(text*2)
# print('x1'+ text[0:-1])


# x=-9
# if x>0:
#     print('正数')
# else:
#     print('非负数')
#

# num1=500
# num2=800
# count=num1+num2
# print(count)


# a=5
# b=6
# x=a  #x=5
# a=b  #a=6
# b=x  #b=51
# print(a,b)

# a=5
# b=6
# a,b=b,a
# print(a,b)

# a=input("请输入a:")
# b=input("请输入b:")
# a,b=b,a
# print('a='+a,'b='+b)

# a,b,c,d=8,9.9,False,3+4j
# print(a,b,c,d)
# print('a的类型为:',type(a)),print('b的类型为:',type(b)),print('c的类型为:',type(c)),print('d的类型为:',type(d))

# a=3.9
# b=6
# print('a=',int(a)),print('b=',float(b))

# a=8
# b=5
# c=0
#
# c=a+b
# print('c1为',c)
# c=a-b
# print('c2为',c)
# c=a/b
# print('c3为',c)
# c=a%b
# print('c4为',c)
# c=a//b
# print('c5为',c)
# c=a**b
# print('c6为',c)

# a=input('请输入a')
# b=input('请输入b')
# if a>=b:
#     print(a)
# else:
#     print(b)

# a=int(input('请输入a'))
# b=int(input('请输入b'))
# if a>=b:
#     print(a)
# else:
#     print(b)

# a=input('请输入a')
# print(type(a))
#
# b=int(float(input('请输入b')))
# print('b=',b,type(b))


# c=int(15.8)
# print(c)

# print(0 and 3)
# print(3 and 0)
# print(3 and 3)
# print(1 and -5)
# print(1 and 2)
# print(2 and 1)

# a=9
# list1=[1,9,15,22,56,78]
# if a in list1:
#     print(True)
# else:
#     print(False)

# a=9
# list1=[1,9,15,22,56,78]
# if a not in list1:
#     print(False)
# else:
#     print(True)

# var =1
# while var ==1:     #永远为ture，无限循环
#     month=int(input('请输入月份'))
#     list_month1=[1,2,3,4,5,6]
#     list_month2=[7,8,9,10,11,12]
#     if month in list_month1:
#         print('输入月份为上半年')
#     elif month in list_month2:
#         print('输入月份为下半年')
#     else:
#         print('输入错误')
#         break      #退出


# for i in range(3):                  #指定循环3次
#     month=int(input('请输入月份'))
#     list_month1=[1,2,3,4,5,6]
#     list_month2=[7,8,9,10,11,12]
#     if month in list_month1:
#         print('输入月份为上半年')
#     elif month in list_month2:
#         print('输入月份为下半年')
#     else:
#         print('输入错误')

# for i in range(5):
#     age=int(input('请输入年龄'))
#     if 18 > age >= 0:
#         print('未成年')
#     elif age >=18:
#         print('已成年')
#     else:
#         print('输入错误')
#         break

# var=1
# while var==1:
#     imonth=int(float(input('请输入月份：')))
#     if 6>=imonth>0:
#         if imonth<=3:
#             print('当前月份为第一季度')
#         else:
#             print('当前月份为第二季度')
#         print('当前月份为上半年')
#     elif 12>=imonth>6:
#         if imonth<=9:
#             print('当前月份为第三季度')
#         else:
#             print('当前月份为第四季度')
#         print('当前月份为下半年')
#     else :
#         print('输入错误')
# #        break


# i=1
# s=0
# while i<=100:
#     i+=1   #i=i+1
#     s+=i   #s=s+1
#     print('i为',i,'s为',s,)


# i=1
# s=0
# while i<=100:
#     s+=i   #s=s+1
#     i+=1   #i=i+1
# print('s为',s,)


# x= int(input('请输入第一个数字:'))
# r=x
# y= int(input('请输入第二个数字:'))
# s=0
# while x <= y:
#     s+=x
#     x+=1
# print('%d 到 %d 的和为：%d'%(r,y,s))


# j=1
# while j<=6:
#     j+=1  #j=j+1
#     i=1
#     while i <=4:
#         print('*',end='*')
#         i+=1
#         print('')


# for i in [9,5,2,7]:
#     print(i)

# s=0
# for i in range(0,101):
#     s+=i
#     print(s)


# str1=['baidu','goole','taobao','pxx']
# for str1 in str1 :
#     print(str1)


# str2=str(input('请输入字符串'))
# for i in str2:
#     print(i)

# for i in range(9):
#     print(i)


# x=int(input('请输入第一个'))
# y=int(input('请输入第二个'))
# z=int(input('请输入步长'))
# for i in range(x,y,z):
#     print(i)


# a=list(range(10))
# print(a)


# n=5
# while n>0:
#     n-=1
#     if n==3:
#         continue
#     print(n)
# print('结束')


# n = 5
# while n < 100:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# print('结束')


# n = 5
# while n < 100:
#     n += 1
#     if n%5==0:  #余数为0
#         continue
#     print(n)
# print('结束')


# for i in range(1,100):
#     if i%7==0:
#         print(i)
# print('结束')


# for i in range(0,100,7):
#     if i >0 and i%7==0:
#         print(i)


# for i in range(0,100,7):
#     if  i%7==0:
#         if i==0:
#             continue
#         print(i)


# list1=[]                  #创建一个列表
# for i in range(0,100,7):
#     list1.append(i)       #使用append在列表中添加元素
# del list1[0]              #删除第0个元素
# print(list1)


# j=1
# while j<=6:
#     j += 1
#     i=1
#     while i<=4:
#         print('*',end='')
#         i+=1
#     print('')


# name="周润发"
# jobs="演员"
# height=180
# weight=75.5
# address="ZH"
# income=10000000
# phone=13800000000
#
#
# #字符串格式化
#  %[name][flag][width][.][precision]type
#   name 可以为空
#   flag   + 右对齐  - 左对齐  # 不同进制前加符号  0 填充
#   width  宽度
#   precision  小数点位
#   type  类型   %d 整形     %s 字符串     %o 八进制    %x 十六进制    %X 大写十六进制    %f 浮点型
# print("-"*70)
# print("|  姓名:  |%35s"%name)
# print("-"*70)
# print("|  职业:  |%34s"%jobs)
# print("-"*70)
# print("|  身高:  |%35dnm"%height)
# print("-"*70)
# print("|  体重:  |%37.2fkg"%weight)
# print("-"*70)
# print("|  住址:  |%34s"%address)
# print("-"*70)
# print("|  收入:  |%43.2f￥"%income)
# print("-"*70)
# print("|  电话:  |%43d"%phone)
# print("-"*70)


# stringtext1='abcdefgabcdefaaa'
# text1=stringtext1.find('def')
# print(text1)
# text2=stringtext1.find('bc',0,1)
# print(text2)
# text3=stringtext1.count('b',0,9)
# print(text3)
# text4=stringtext1.replace('a','c')
# print(text4)
# a,b,c=stringtext1.split('b')
# print(a+'\n'+b+'\n'+c+'\n')


# c=3+5
# print(f'c={3+5}')
# print('c={3+5}')


# stringtext12='one two three'
# text6=stringtext12.split()
# print(text6)


# list1=[1,2,3,4,'a','b','c']
# print(list1)
#
# tuple1=(1,2,3,4,'a','b','c,')
# print(tuple1)
#
# dict1={'a':1,'b':2,'c':3}
# print(dict1)


# name='Want to go'
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.swapcase())

# list_text1=['老王','老王的狗','猫','a','abc','1','1234']
# print(list_text1)
# for i in list_text1:
#     print(i)
# print(list_text1[1])


# list_text2=['老王','老王的狗','猫','a','abc','1','1234','终要走']
# i=0
# while i<8:
#     print(list_text2[i])
#     i+=1


# list_text3=['老王','老王的狗','猫','a','abc','1','1234','终要走','再见']
# list_text3.append('难得')
# list_text3.insert(2,'人员')
# list_text4=['天气','冰雪','大暑']
# list_text3.extend(list_text4)
# i=0
# j=len(list_text3)
# while i<j:
#     print(list_text3[i])
#     i+=1


# list_text3=['老王','老王的狗','猫','a','abc','1','1234','终要走','再见']
# copy1=list_text3.copy()
# print(copy1)
# copy2=copy.copy(list_text3)
# print(copy2)
# list_text3.remove('老王的狗')
# print(list_text3)
# del list_text3[0]
# print(list_text3)
# list_text3[3]='101'
# print(list_text3)


# list_text7=[9,5,2,7,6]
# list_text7.sort()
# print(list_text7)
# list_text7.sort(reverse=True)
# print(list_text7)
# list_text7.reverse()
# print(list_text7)


# list_text8=[0,9,5,2,7,6,8,4]
# y=sorted(list_text8)
# print(list_text8)
# print(y)


# tuple_text1=('123','abc','铁塔')
# print(tuple_text1)
# # for i in tuple_text1:
# #     print(i)
# print(len(tuple_text1))
# print(max(tuple_text1))
# print(min(tuple_text1))
# list_text9=['456','def','天天']
# print(tuple(list_text9))


# string_text1='123456'
# print(string_text1)
# string_text2=string_text1
# listing_text1=list(string_text1) #字符串转换为列表
# print('字符串转换为列表',listing_text1)
# print(type(listing_text1))
# string_text3=str(listing_text1) #列表转换为字符串
# print('列表转换为字符串',string_text3)
# print(type(string_text3))
# string_text5=string_text3.replace("'",'')
# #print(string_text5)
# string_text5=string_text5.replace(",",'')
# #print(string_text5)
# string_text5=string_text5.replace(" ",'')
# #print(string_text5)
# string_text5=string_text5.strip(' ,[]')
# print('处理后的字符串',string_text5)
# # if string_text5 ==string_text1:
# #     print(True)
# # else:
# #     print(False)
# tupleing_text1=tuple(string_text2)#字符串转换为元组
# print('字符串转换为元组',tupleing_text1)
# print(type(tupleing_text1))
# listing_text11=[1,2,3,4,5,6]
# tupleing_text2=tuple(listing_text11)#列表转换为元组
# print('列表转换为元组',tupleing_text2)
# print(type(tupleing_text2))
# listing_text12=list(tupleing_text2)
# print('元组转换为列表',listing_text12)
# print(type(listing_text12))


# dict_text1={"陵园":"北山","ID":257,"面积":"BIG"}
# print(dict_text1)
# print(dict_text1["ID"])
# dict_text1["ID"]="258"
# print(dict_text1)
# dict_text1["年限"]="100年"
# print(dict_text1)
# del dict_text1["年限"]
# print(dict_text1)
# dict_text1.clear()
# print(dict_text1)
# print(len(dict_text1))
# for i  in dict_text1:
#     print(i)
# for i  in dict_text1.values():
#     print(i)
# for i  in dict_text1.items():
#     print(i)


# def add():
#     a = float(input('请输入a:'))
#     b = float(input('请输入b:'))
#     c = a+b
#     print("%.2f+%.2f=%.2f"%(a,b,c))
# add()


# def add():
#     a = float(input('请输入a:'))
#     b = float(input('请输入b:'))
#     c =a+b
#     print(c)
# add()

# def add_text():
#     c=11+22
#     print(c)
# add_text()

# def add_text1(a,b):
#     c=a+b
#     print(c)
# add_text1(11,12)

# def add_text2(a, b):
#     s = a + b
#     print("%.2f+%.2f=%.2f" % (a, b, s))
#     # a = float(input("请输入a："))
#     # b = float(input("请输入b："))
#     # d = a + b
#     # print("%.2f+%.2f=%.2f" % (a, b, d))
# add_text2(3, 5)

# def add_text3(b,c,a=1):
#     s=a+b+c
#     print("%.2f+%.2f+%.2f=%.2f"%(a,b,c,s))
# add_text3(3,6,8)


# def yuan():
#     r=6
#     PI=3.14
#     S=PI*r*r
#     print(S)
# yuan()


# def add_text4(a,b,*args):
#     print(a,b,*args)
# add_text4(1,2,6,9)


# def textB():
#     print("textB开始")
#     print("textB内容")
#     print("textB结束")
# def textA():
#     print("textA开始")
#     print("textA内容")
#     textB()
#     print("textA结束")
# textA()


# def jiechen(n):
#     if n==1 :
#         return 1
#     else:
#         return n*jiechen(n-1)
# print(jiechen(5))
# jiechen(5)


# n = int(input("请输入一个整数:"))
# def jiechen(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*jiechen(n-1)
# print(jiechen(2))


# a=10
# def text_one():
#     a=100
#     print(a)
# text_one()


# import time
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d   %H:%M:%S",time.localtime()))
# print(time.strftime("%y-%m-%d   %H:%M:%S",time.localtime()))

# import calendar
# a=calendar.month(2019,2)
# print(a)
# b=calendar.calendar(2023)
# print(b)


#file_text=open("E:/pypro/text1.txt","w")
# file_text=open("../pypro/text1.txt","a")
# file_text.write("草长莺飞二月天\n")
# file_text.write("春风吹又生\n")
# file_text.write("白云知我意")
#
# file_text=open("text1.txt","r")
# text=file_text.read()
# text=file_text.readline()
# print(text)

#import os
# os.rename("../pypro/text1.txt","text0.txt")
# os.remove("text0.txt")
# os.mkdir("../9527")
# os.rmdir("../9527")


# list_1=["das","dbs"]
# print(list_1[1])



# try:
#     num_1=int(input("输入第一个数"))
#     num_2=int(input("输入第二个数"))
#     s=num_1/num_2
#     print(s)
# except:
#     print("除数不能为0")



# import math
# a= int(input("输入数"))
# print(math.sqrt(a))
#

# import test2
# print(test2.add_text5(3,5))

# from test2 import add_text5,add_text6
# print(add_text6(5,3))
# print(add_text5(2,7))


# import xlrd2
# filepath=r'../pypro/20230103.xls'
# date=xlrd2.open_workbook(filepath,"r")
# table=date.sheets()[0]
# num_rows=table.nrows
# print(num_rows)
# num_cols=table.ncols
# print(num_cols)
# for row in  range(num_rows):
#     for col in range(num_cols):
#         value=table.cell_value(row,col)
#         print("第%d行%d列的数据为:%s"%(row+1,col+1,value))
# value=table.cell_value(rowx=0,colx=1)  #获取值
# print(value)
# value=table.cell(rowx=0,colx=1)  #获取对象和值
# print(value)

# class Cat:
#     def __init__(self):  #/构造函数，初始化属性
#         self.color="白色"
#         self.age="7"
#     def eat(self):
#         print("吃老鼠")
#     def sing(self):
#         print("喵喵喵")
# jiafeimaoA=Cat()
# jiafeimaoA.eat()
# jiafeimaoA.sing()
# print(jiafeimaoA.color)
# print(jiafeimaoA.age)

# import time
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print("已释放资源")
# zhangsan=Person("张三",25)
# print(zhangsan.name,zhangsan.age)
# print("3秒后释放资源")
# time.sleep(3)
# zhangsan=Person("李四",28)
# print(zhangsan.name,zhangsan.age)

#夕阳西下，金色的宝马在路上飞驰
# class Car:
#     def __init__(self,color,car_name):
#         self.color=color
#         self.car_name=car_name
#     def sport(self):
#         print("飞驰")
# text=Car("金色","宝马")
# print("夕阳西下，%s的%s在路上"%(text.color,text.car_name),end="")
# text.sport()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age   #私有属性
#     def set_age(self,maxage):  #set 设置私有属性
#         self._age=maxage
#     def get_age(self):         #get 获取私有属性
#         if 0<self._age<120:
#             return self._age
#         else:
#             print("年龄错误")
# people=Person("李四",28)
# print(people.get_age())


# class Cat(object):
#     def __init__(self,color='蓝色'):
#         self.color=color
#     def sing(self):
#         print("抓老鼠")
# class LanCat(Cat):
#     def relax(self):
#         print("休息")
#     def sun(self):
#         print("晒太阳")
# TOM=LanCat()
# print("%s的猫正在"%(TOM.color),end="")
# TOM.sing()
# TOM.relax()
# TOM.sun()


print("hello world!")

def aaa():
    print("sss")

def main():
    print("xxx")

if __name__=='__main__':
    aaa()
    main()
    print("now__name__is %s" %__name__)