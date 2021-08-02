#输入：x = 123
#输出：321


def reverse(x):
    rev=0

    while x !=0:

        dight=x%10
        #Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
        if x<0 and dight >0:
            dight-=10
        x=(x-dight)//10
        rev=rev*10+dight

    return rev

print(reverse(-12))