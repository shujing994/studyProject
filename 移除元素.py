#给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

#输入：nums = [3,2,2,3], val = 3
#输出：2, nums = [2,2]
class Solution:
    def func(self,nums,val):
        for i in  nums:
            if i==val:
                nums.remove(i)

        return print(len(nums))

s=Solution()
nums=[3,2,2,3,5]
val=3
s.func(nums,val)
