import unittest
import collections

class unitest(unittest.TestCase):
    def testNone(self):
        nums1 = []
        nums2 = []
        Output = []
        self.assertEqual(Solution().intersect(nums1,nums2),Output)
    def testSample(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2, 2]
        Output = [2, 2]
        self.assertEqual(Solution().intersect(nums1,nums2),Output)

class Solution():
    def intersect(self, nums1, nums2):
        C = collections.Counter
        return list((C(nums1) & C(nums2)).elements())

if __name__ == '__main__':
    unittest.main()
