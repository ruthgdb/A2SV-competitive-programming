class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        first, second, res = 0, 0, []
        
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                res.append(nums1[first])
                first += 1
                second += 1
            elif nums1[first] < nums2[second]:
                first += 1
            elif nums1[first] > nums2[second]:
                second += 1
                
        return res
