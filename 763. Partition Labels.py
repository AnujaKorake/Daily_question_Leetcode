class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
    
        partitions = []
        start, end = 0, 0

        # Step 2: Iterate through the string to find partitions
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Expand partition if needed

            # Step 3: If we reach the end of a partition
            if i == end:
                partitions.append(end - start + 1)  # Store partition size
                start = i + 1  # Move to the next partition

        return partitions

solved this question by using youtube solution.