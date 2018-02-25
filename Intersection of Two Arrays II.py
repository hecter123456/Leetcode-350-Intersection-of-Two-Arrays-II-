import unittest

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
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        List = []
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                List.append(nums1[i])
                i += 1
                j += 1
        return List

if __name__ == '__main__':
    unittest.main()
