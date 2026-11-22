class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sl=sorted(nums1+nums2)
        if len(sl)%2==0:
            return (sl[len(sl)//2]+sl[(len(sl)//2)-1])/2
        else:
            return sl[len(sl)//2]