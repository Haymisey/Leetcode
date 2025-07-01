class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=len(nums1)-1
        p1=m-1
        p2=n-1
        while p1>=0 and p2>=0:
            n1,n2=nums1[p1],nums2[p2]
            if n1>n2:
                nums1[l]=n1
                p1-=1
                l-=1
            else:
                nums1[l]=n2
                p2-=1
                l-=1
        while p2>=0:
            nums1[l]=nums2[p2]
            p2-=1
            l-=1            
               
