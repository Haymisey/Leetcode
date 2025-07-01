class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        i=2
        while i<len(nums):
            if nums[i]==nums[i-1] and nums[i]==nums[j]:
                nums.pop(i)
            else:
                j+=1
                i+=1
        return len(nums)    