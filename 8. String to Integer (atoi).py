link: https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ''
        s = s.strip()  

        if not s:  
            return 0

        sign = 1
        if s[0] in ('-', '+'):  
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for i in s:  
            if i.isdigit():
                temp += i   
            else:
                break  

        if temp == '':  
            return 0


        # ✅ Step 4: Clamp the value within the 32-bit integer range using by chatgpt
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result

            
        
            