#lambda函数的定义和调用

def func(x):
    return x


ident=lambda  x:x

print(ident(3))

#lambda函数也有自己的独有性质，即lambda函数可以使用立即调用的函数表达形式(IIFE)。
# 我们可以在定义lambda函数的同时进行调用，此时lambda函数也不再需要一个用于调用的函数名了
print((lambda x:x+1)(3))

#lambda函数因为其简单的定义方式，在很多高阶函数的定义中会被使用。tips: 高阶函数即，函数存在至少一个参数是函数且该函数的返回值是一个函数。
high_func=lambda x,func: x+func(x)
print(high_func(2,lambda x:x*x))

#lambda的递归调用。将一个整数n，拆分打印出来。如234，应2，3，4分三行打印出来。
n=int(input('请输入一串数字：'))

f=lambda a,f:(a/10)!=0 and f(int(a/10),f) or (a!=0 and print('%d' %(a%10)))
#f(n,f)

#一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程：找出1000以内的所有完数。
factors=lambda x :filter(lambda i:x%i==0 and i,range(1,x))
f=lambda x:sum(factors(x))==x
print([(i,list(factors(i))) for i in list(filter(f,range(2,10001)))])

