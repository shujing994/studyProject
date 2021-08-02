#找出两个字符串中最大公共子字符串，如"abjeccarde"，"sjdgcargde"的最大子串为"car"
#1.先遍历a的子字符串
#2.判断a的子字符串同时也在字符串b里，添加到f列表
#3.最后f列表里面取出最后一个，就是最长的子串了

a='casbshujingojsdihnfja'
b='sdasdbbshujing123'

f=[]
for i in range(1,len(a)+1):
    #j是下标位置
    for j in range(len(a)+1-i):
        e=a[j:j+i]
        if e in b:
             f.append(e)

print(f)
print(f[-1])


for i in range(1,len(a)+1):
    for j in range(len(a)+1-i):
        e=a[j:j+i]
        if e in b:
            f.append(e)
            
