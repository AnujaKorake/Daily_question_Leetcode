from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # No triplet possible
        
        # Step 1: Compute prefix max array
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # Step 2: Compute suffix max array
        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])

        # Step 3: Iterate over j and compute the max triplet value
        max_value = 0
        for j in range(1, n - 1):
            max_i = prefix_max[j - 1]  # max before j
            max_k = suffix_max[j + 1]  # max after j
            max_value = max(max_value, (max_i - nums[j]) * max_k)

        return max_value