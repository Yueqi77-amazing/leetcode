#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串 
# @param version2 string字符串 
# @return int整型
#
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        # write code here
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1,n2 = len(nums1),len(nums2)
        for i in range(max(n1,n2)):
            v1 = int(nums1[i]) if i < n1 else 0
            v2 = int(nums2[i]) if i < n2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
if __name__ == '__main__':
    version1 = "1.0.0"
    version2 = "1.0"
    s = Solution()
    print(s.compare(version1,version2))