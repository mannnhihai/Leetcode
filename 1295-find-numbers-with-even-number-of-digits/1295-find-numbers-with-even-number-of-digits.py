class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for nums in nums:
            str(nums) 
            digit =str(nums)
            digit_count = len(digit)
            if digit_count % 2 == 0:
                count +=1
             
           
           

        return count

        