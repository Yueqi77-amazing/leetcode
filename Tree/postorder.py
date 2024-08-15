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
    def postorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        res,s =[],[]
        pre = None
        while root or s:
            while root:
                s.append(root)
                root = root.left
            node = s[-1]
            s.pop()
            if node.right is None or node.right == pre:
                res.append(node.val)
                pre = node
            else:
                s.append(node)
                root = node.right
        return res
    def postorderTraversal1(self , root: TreeNode) -> List[int]:
        # write code here
        res = []
        self.postOrder(res,root)
        return res
    def postOrder(self,res:List[int],root:TreeNode):
        if root is None:
            return
        self.postOrder(res,root.left)
        self.postOrder(res,root.right)
        res.append(root.val)
        return res
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.postorderTraversal(root))
    