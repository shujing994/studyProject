#1.比较相邻的元素，如果第一个比第二个大，就交换他们两个

#2.对每一对相邻的元素都进行比较，从第一对到最后一对。这时，最后的元素就是最大的数。

'''list=[3,5,2,4,7,1,9,3,5,8]

def pai_xu(list):
    n=len(list)
    for j in range(0,n-1):
        for i in range(0,n-1-j):
            if list[i]>list[j]:
                list[i],list[i+1]=list[i+1],list[i]

pai_xu(list)
print(list)'''

list1 = [4,2,7,1]

def func(list1):

    list1.sort()
    print(list1)
    n=len(list1)
    score=int(input('请输入数字： '))

    for j in range (0,n-1):
        for i in range(0,n-1-j):
            if list1[i]>= score >list1[j]:
                print(i+1)

func(list1)
