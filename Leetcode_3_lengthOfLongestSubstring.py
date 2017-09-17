import time

class Solution(object):
    def __init__(self):
        pass
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def check_re(subs):
            len_subs = len(subs)
            len_set = len(set(subs))
            if len_subs==len_set:
                return 1
            else:
                return 0
        
        total_string_length = len(s)
        longest_string_length = 0
        substring_length = 0
        index = 1
        i=0
        count=0
        ans_string=''
        
        if s == '':
            return 0
        
        elif len(s)==1:
            return 1
        
        else:
            while index < total_string_length:
                count += 1
                sub = s[i:index+1]
                #print(sub)
                substring_length = len(sub)
                
                #引入判讀函數，跳接才會快
                if not check_re(sub):
                    for k in range(0, index-i):
                        #如果sub是有重複的話的的話，闖關失敗直接跳出迴圈，變且這次的len(sub)要減掉1
                        if sub[k] == sub[-1]:
                            #print('F')
                            i += k+1
                            #index += k
                            substring_length = len(sub)-1
                            break
                
                #冠軍交關之際，就紀錄答案字串和長短
                if substring_length > longest_string_length:
                    longest_string_length = substring_length
                    ans_string = sub
                
                index += 1
        
        print(count)
        print('max:', longest_string_length)
        print(ans_string)
        return longest_string_length
    
start = time.time()
test = 'abcdefghijklmnoprvbnm1234567890[]\;/.,QWERTYUIOPLKJHGFDSAZXCVBNM'*10000+'z'

S=Solution()
S.lengthOfLongestSubstring(test)

end = time.time()
print(end-start)