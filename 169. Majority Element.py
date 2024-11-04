#problem statement link: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

#solution 1:  (Time limit Exeeds)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums)/2 
        coun = []
        for i in nums:
            coun.append(nums.count(i))

        if max(coun) > c:
            return nums[coun.index(max(coun))]


#solution 2:

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # Step 1: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Step 2: Return the candidate
        return candidate
