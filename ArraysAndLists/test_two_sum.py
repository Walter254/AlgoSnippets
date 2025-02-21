import unittest
from two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_basic_cases(self):
        # Test the examples provided in the original problem
        self.assertEqual(two_sum([2,7,11,15], 9), [0,1])
        self.assertEqual(two_sum([3,2,4], 6), [1,2])
        self.assertEqual(two_sum([3,3], 6), [0,1])

    def test_zero_values(self):
        # Test with zeros
        self.assertEqual(two_sum([0,0], 0), [0,1])
        self.assertEqual(two_sum([0,1,2], 2), [0,2])

    def test_larger_numbers(self):
        # Test with larger numbers
        self.assertEqual(two_sum([1000,2000,3000], 5000), [1,2])
        self.assertEqual(two_sum([999999,1000000], 1999999), [0,1])


    def test_edge_cases(self):
        # Test minimal valid input
        self.assertEqual(two_sum([1,2], 3), [0,1])
        
        # Test with duplicate numbers (but not same index)
        self.assertEqual(two_sum([5,5,5,5], 10), [0,1])

if __name__ == '__main__':
    unittest.main()