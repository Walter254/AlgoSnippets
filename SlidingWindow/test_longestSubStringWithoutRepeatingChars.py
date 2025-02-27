import unittest
from longestSubStringWithoutRepeatingChars import longestSubStringWithoutRepeatingChars

class TestLongestSubStringWithoutRepeatingChars(unittest.TestCase):
    
    def test_example_cases(self):
        # Example 1
        self.assertEqual(longestSubStringWithoutRepeatingChars("abcabcbb"), 3)
        # Example 2
        self.assertEqual(longestSubStringWithoutRepeatingChars("bbbbb"), 1)
        # Example 3
        self.assertEqual(longestSubStringWithoutRepeatingChars("pwwkew"), 3)

    def test_edge_cases(self):
        # Edge case: empty string
        self.assertEqual(longestSubStringWithoutRepeatingChars(""), 0)
        # Edge case: string with all unique characters
        self.assertEqual(longestSubStringWithoutRepeatingChars("abcdef"), 6)
        # Edge case: string with special characters
        self.assertEqual(longestSubStringWithoutRepeatingChars("!@#$%^&*()"), 10)

if __name__ == '__main__':
    unittest.main() 