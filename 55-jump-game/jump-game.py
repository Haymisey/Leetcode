class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)-1
        p=l-1
        while p>=0:
            if nums[p]>=l-p:
                l=p
                p-=1
            else:
                p-=1
        if p==l-1:
            return True
        return False            
           
