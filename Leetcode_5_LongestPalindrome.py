#指定index往兩側檢驗是否可以符合回文
#優化：不要每次有人過關就跑一次dict阿，你只需要記住他在字典上的index就好了，最後用max_sub一次取出！！ 通過!!

import time

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        total_length = len(s)
        s_dict = {}
        for i in range(total_length):
            s_dict[i]=s[i]
            
        max_subs = {}
        max_subs_tags = [0,0]
        subs_tags = [0,0]
        longest_length_subs = index = len_subs = 0
        
        for index in range(total_length): #這是回文字串假設為奇數的情形
            for x in range(0, min(index+1, total_length-index)):
                #print('index', index)
                
                if s_dict[index - x] != s_dict[index + x]: #錯誤就直接跳出
                    break
                
                else: #如果沒有錯，舊紀錄頭尾的字典標籤
                    subs_tags[0] = index-x
                    subs_tags[1] = index+x
                    len_subs = 2*x+1
                    #print('subs_tags:', subs_tags)
                    
                    if len_subs > longest_length_subs:
                        longest_length_subs = len_subs
                        max_subs_tags = subs_tags[:]  #注意list要對貼之前，一定要只有複製該元素，否則會跟著改動
                        #print('max_subs_tags:', max_subs_tags)
                        
            if index + longest_length_subs//2 > total_length: #提早跳出迴圈
                break
        
        #print(max_subs_tags)
        print('奇數檢查完畢')
        
        for index in range(total_length): #這是回文字串假設為偶數的情形
            for x in range(0, min( index+1, total_length -index-1 )):
                #print('index', index)
                
                if s_dict[index - x] != s_dict[index+1 + x]:
                    break
                
                else:
                    subs_tags[0] = index-x
                    subs_tags[1] = index+1+x
                    len_subs = 2*x+2
                    #print('subs_tags:', subs_tags)
                    
                    if len_subs > longest_length_subs:
                        longest_length_subs = len_subs
                        max_subs_tags = subs_tags[:] #注意list要對貼之前，一定要只有複製該元素，否則會跟著改動
                        #print('max_subs_tags:', max_subs_tags)
                        
            if index + longest_length_subs//2 > total_length: #提早跳出迴圈
                break
        
        #print(max_subs_tags)
        print('偶數檢查完畢')
        
        #該是取出tags的時候了
        max_subs = { k:s_dict[k] for k in range(max_subs_tags[0] , max_subs_tags[1]+1) }
        #print(max_subs)
        
        sd = sorted(max_subs.items())
        max_subs_str = ''.join('{}'.format(val) for key, val in sd) #把dict變成str
        print('max subs:', max_subs_str)
        return max_subs_str
        
start = time.time()
test = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


S=Solution()
S.longestPalindrome(test)

end = time.time()
print(end-start)