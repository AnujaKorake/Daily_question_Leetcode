#problem statement link: https://leetcode.com/problems/continuous-subarray-sum/description/?envType=daily-question&envId=2024-11-04

#solution:

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: -1} 
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            if k != 0:
                prefix_sum %= k
            
            if prefix_sum in mod_map:
                if i - mod_map[prefix_sum] > 1:
                    return True
            else:
                mod_map[prefix_sum] = i
        
        return False