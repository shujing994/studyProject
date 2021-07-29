#python判断一个字符串是否为另一字符串的子串的几种方法

#用in方法
#ss=input('请输入： ')
#sl=input('请输入： ')

#print(ss in sl)

#使用string模块的find()方法

import string

s='123shujing456'
t='shujing'

result= str.find(s,t)!= -1
print(result)

#string函数
#大小写处理
str.upper(s)
str.lower(s)
print(s)
#大小写互换
str.swapcase(s)
#首字母大写，其余小写
str.capitalize(s)
#字符串搜索相关
str.find(s,'123')  #搜索指定字符串，没有返回-1
str.index(s,'123')
str.rfind(s,'123')  #从右边开始查找
print(str.count(s,'shu')) #统计指定的字符串出现的次数

str.strip(s)  #去两边空格



