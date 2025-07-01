class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      j=0
      repeated=[]
      repeated.append(nums[0])
      for i in range(1,len(nums)):
        if nums[i] in repeated:
            nums[i]='_'
            j+=1
        repeated.append(nums[i])
      for i in range(j):
        nums.remove('_')
      k=len(nums)          