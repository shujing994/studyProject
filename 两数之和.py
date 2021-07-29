#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#输入：nums = [2,7,11,15], target = 9
#输出：[0,1]
#解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

#思路：挨个遍历，并且判断  num2 = target - num1，是否也在 list 中

'''def func(nums,target):

    lens=len(nums)
    result=[]

    for i in range(lens):
        for j in range(i+1,lens):
            if nums[i]+nums[j]==target:
                result.append((i+1,j+1))
    return result

print(func([2,5,7,3,4],7))'''


#哈希字典
def func1(nums,target):
    result1=[]
    dict_y={}
    for i in range(len(nums)):
        m=nums[i]
        if target-m in nums:
            result1.append((dict_y[target-m]+1,i+1))
            dict_y[m]=i
    return result1

print(func1([2,5,7],7))

#使用字典进行存储





