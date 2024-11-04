#problem statement link : https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        for i in range(nums.count(val)):
            nums.remove(val)

        nums += ['_'] * nums.count(val)