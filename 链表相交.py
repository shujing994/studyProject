#编写程序，找到两个单链表相交的起始节点

#输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
#输出：Reference of the node with value = 8
#输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起
# ，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


#使用集合
class Solution():
    def func(self,headA,headB):

        s=set()
        h1=headA
        h2=headB

        while h1:
            s.add(h1)
            h1= h1.next
        while h2:
            if h2 in s:
                break
            h2=h2.next
        return h2

if __name__ == '__main__':
    solution=Solution()
    head1=[1,2,3,4,5]
    head2=[4,5,6,7]
    solution.func(head1,head2)