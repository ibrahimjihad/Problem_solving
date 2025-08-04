class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        while k<len(nums):
            if nums[k]==nums[k-1]:
                del nums[k]
                k-=1
            k+=1
    

        
        