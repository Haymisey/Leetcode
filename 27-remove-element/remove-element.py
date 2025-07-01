class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=nums.count(val)
        for i in range(j):
            nums.remove(val)
        k=len(nums)