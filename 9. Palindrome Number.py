link:https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        s1 = s[::-1]
        if s == s1:
            return True
        else:
            return False