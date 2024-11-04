#problem statement link: https://leetcode.com/problems/string-compression-iii/description/?envType=daily-question&envId=2024-11-04

#solution:

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        i = 0
        n = len(word)

        while i < n:
            count = 1
            while i + count < n and word[i] == word[i + count]:
                count += 1  
            temp_count = count
            while temp_count > 9:
                comp += '9' + word[i]
                temp_count -= 9
            comp += str(temp_count) + word[i]

            i += count  

        return comp
