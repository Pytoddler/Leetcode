class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #遞回尋找排序後的真實數字
        def answer_values(nums, target):
            total_nums = len(nums)
            index_ans=[]
            sorted_nums = sorted(nums)
            
            for i in range(total_nums):
                for j in range(i+1, total_nums):
                    if int(sorted_nums[i])+int(sorted_nums[j]) == target:
                        num1 = sorted_nums[i]
                        num2 = sorted_nums[j]
                        return num1, num2
                        break
                    
                    elif int(sorted_nums[i])+int(sorted_nums[j]) > target:
                        break
                    
                    else:
                        pass
                    
                    
        def return_index(nums, num1, num2):
            ans_list = []
            
            if num1 == num2:
                for i , value in enumerate(nums):
                    if value == num1:
                        ans_list.append(i)
                    else:
                        pass
                        
                    if len(ans_list) == 2:
                        break
            
            else:
                for i , value in enumerate(nums) :
                    if value == num1:
                        ans_list.append(i)
                    elif value == num2:
                        ans_list.append(i)
                    else:
                        pass
                    
                    if len(ans_list) == 2:
                        break
                    
            return ans_list

        num1, num2 = answer_values(nums, target) 
        
        return return_index(nums, num1, num2)

    
S = Solution()
print(S.twoSum([0,3,0],0))
