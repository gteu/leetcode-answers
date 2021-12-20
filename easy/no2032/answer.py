class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ns1, ns2, ns3 = set(nums1), set(nums2), set(nums3)
        return list((ns1 & ns2) | (ns2 & ns3) | (ns3 & ns1))
