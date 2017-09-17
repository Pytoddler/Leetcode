import time

class Solution(object):
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        x_str = str(abs(x)) #先取絕對值
        reversed_x = x_str[::-1]
        
        if x >= 0:
            ans_int = int(reversed_x)   
        else:
            ans_int = int(reversed_x) * (-1)
        
        #注意沒有sign可以放到2**32，如果有sign的話只能到+/-2**31
        if ans_int>int(2**31) or ans_int<int(-2**31): 
            ans_int = 0
        else:
            pass
        
        print(ans_int)
        return ans_int
    

start = time.time()
test = int(-15741222222)

S=Solution()
S.reverse(test)

end = time.time()
print(end-start)