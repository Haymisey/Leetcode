class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums[:]=sorted(nums)
        j=0
        i=0
        diff=0
        ans=0
        while j < len(nums):
            if nums[j]!=nums[i] and j-i>diff:
                diff=j-i
                ans=nums[i]
                i=j
                j+=1
            else:
                j+=1
        if j-i>diff:
            ans=nums[i]
        return ans            

