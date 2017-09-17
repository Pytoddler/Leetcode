import time

class Solution(object):
    def __init__(self):
        pass
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        B = True
        s = str(x)
        length = len(s)
        
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                B = False
                break
        
        print(B)
        return B
        
        
start = time.time()
test = 'dcbavacavabcd'

S=Solution()
S.isPalindrome(test)

end = time.time()
print(end-start)