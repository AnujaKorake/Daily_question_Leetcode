#my solution :
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')
        while i < j:
            if s[i] in vowels: 
                if s[j] in vowels :
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
            
        return ''.join()





#chatgpt solution :
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')
        while i < j:
            if s[i] not in vowels: 
                    i += 1
            elif s[j] not in vowels: 
                    j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        return ''.join(s)