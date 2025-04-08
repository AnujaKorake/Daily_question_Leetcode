from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        while len(nums) > 0:
            counter = Counter(nums)
            if all(count == 1 for count in counter.values()):
                break
            else:
                nums = nums[3:]  
                operations += 1

        return operations

