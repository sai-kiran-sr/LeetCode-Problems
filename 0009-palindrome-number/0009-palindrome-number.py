class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
    
        y = 0
        temp = x
        
        while temp:
            y = (y * 10) + (temp % 10)
            temp //= 10  #  10 // 3 ==> 3
        
        return x == y
        
        