#problem statement link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>2:
                while nums.count(i) > 2:
                    nums.remove(i)

        return len(nums)