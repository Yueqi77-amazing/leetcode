#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
from typing import List


class Solution:
    def InversePairs(self , nums: List[int]) -> int:
        # write code here
        def mergeSort(data):
            n = len(data)
            if n <= 1:
                return data,0
            l,r =0,0
            m = n//2
            left,leftInverse= mergeSort(data[:m])
            right,rightInverse = mergeSort(data[m:])
            res = []
            countInverse = leftInverse+rightInverse
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    countInverse += len(left)-l
                    r += 1
            res += left[l:]
            res += right[r:]
            return res,countInverse
        orderlist,count = mergeSort(nums)
        return count%(10**9+7)
            
    
if __name__ == '__main__':
    
    nums = [1,2,3,4,5,6,7,0]
    s = Solution()
    print(s.InversePairs(nums))