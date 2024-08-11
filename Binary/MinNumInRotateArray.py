#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
from typing import List


class Solution:
    def minNumberInRotateArray(self , nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l=0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                # 3,3,3,3,3,1,2,3,3,3
                l += 1
                
        return nums[l]
        
    
if __name__ == '__main__':
    nums = [3,4,5,1,2]
    s = Solution()
    print(s.minNumberInRotateArray(nums))
            