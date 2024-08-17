class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 
# @param pRootOfTree TreeNode类 
# @return TreeNode类
#
class Solution:
    def Convert(self , pRootOfTree ):
        # write code here
        if not pRootOfTree:
            return None
        s = []
        head = None
        pre = None
        isFirst= True
        while pRootOfTree or s:
            while pRootOfTree:
                s.append(pRootOfTree)
                pRootOfTree= pRootOfTree.left
            pRootOfTree = s[-1]
            s.pop()
            if isFirst:
                head = pRootOfTree
                pre = head
                isFirst = False
            else:
                pre.right =pRootOfTree
                pRootOfTree.left = pre
                pre = pRootOfTree
            pRootOfTree = pRootOfTree.right
        return head