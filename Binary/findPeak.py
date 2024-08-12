#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
from typing import List


class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        p=[0]*(len(nums)+2)
        p[0]=-10000
        p[len(nums)]=-10000
        p[1:len(nums)-1]=nums
        for k in range(1,len(nums)+1):
            if p[k]>p[k-1] and p[k]>p[k+1]:
                return k-1
            
        return -1
    
if __name__ == '__main__':
    nums = [1,2,3,1]
    s = Solution()
    print(s.findPeakElement(nums))
    