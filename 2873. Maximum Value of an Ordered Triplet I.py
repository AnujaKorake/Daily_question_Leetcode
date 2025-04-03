class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prod = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    prod = max(prod, (nums[i] - nums[j]) * nums[k])
        if prod < 0:
            return 0
        else:
            return prod

