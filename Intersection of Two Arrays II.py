import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        nums1 = []
        nums2 = []
        Output = []
        self.assertEqual(Solution().intersect(nums1,nums2),Output)

class Solution():
    def intersect(self, nums1, nums2):
        if nums1 == [] and nums2 == []:
            return []
        return (nums2 in nums1)

if __name__ == '__main__':
    unittest.main()
