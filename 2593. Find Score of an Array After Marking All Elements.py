import heapq

class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        marked = [False] * n  # To track marked elements
        min_heap = [(nums[i], i) for i in range(n)]  # Create a min-heap with (value, index)
        heapq.heapify(min_heap)  # Convert list to a min-heap
        score = 0

        while min_heap:
            # Extract the smallest unmarked element
            value, index = heapq.heappop(min_heap)
            if marked[index]:
                continue  # Skip if already marked

            # Add its value to the score
            score += value

            # Mark the current element and its neighbors
            if index > 0:
                marked[index - 1] = True
            marked[index] = True
            if index < n - 1:
                marked[index + 1] = True

        return score
