from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return int整型一维数组
#
class Solution:
    def preorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        List = []
        return self.preOrder(List,root)
    def preOrder(self,list:List[int],root:TreeNode):
        if root is None:
            return
        list.append(root.val)
        self.preOrder(list,root.left)
        self.preOrder(list,root.right)
        return list
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.preorderTraversal(root))