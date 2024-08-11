#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
from typing import List


class Solution:
    def search(self , nums: List[int], target: int) -> int:
        l =0
        r = len(nums)-1
        while l<= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return -1
                
                
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    target = 3
    s = Solution()
    print(s.search(nums, target))