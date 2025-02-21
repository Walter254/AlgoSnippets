import unittest
from designHashMap import MyHashMap

class TestMyHashMap(unittest.TestCase):
    def setUp(self):
        """Create a new HashMap instance before each test"""
        self.hashMap = MyHashMap()

    def test_put_and_get(self):
        """Test basic put and get operations"""
        self.hashMap.put(1, 1)
        self.assertEqual(self.hashMap.get(1), 1)
        
        # Test updating existing key
        self.hashMap.put(1, 2)
        self.assertEqual(self.hashMap.get(1), 2)

    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist"""
        self.assertEqual(self.hashMap.get(1), -1)

    def test_remove(self):
        """Test remove operation"""
        self.hashMap.put(1, 1)
        self.hashMap.remove(1)
        self.assertEqual(self.hashMap.get(1), -1)

    def test_example_from_problem(self):
        """Test the example given in the problem description"""
        self.hashMap.put(1, 1)
        self.hashMap.put(2, 2)
        self.assertEqual(self.hashMap.get(1), 1)
        self.assertEqual(self.hashMap.get(3), -1)
        self.hashMap.put(2, 1)
        self.assertEqual(self.hashMap.get(2), 1)
        self.hashMap.remove(2)
        self.assertEqual(self.hashMap.get(2), -1)

    def test_edge_cases(self):
        """Test edge cases with boundary values"""
        # Test with constraint boundaries (0 <= key, value <= 10^6)
        self.hashMap.put(0, 0)
        self.assertEqual(self.hashMap.get(0), 0)
        
        self.hashMap.put(1000000, 1000000)
        self.assertEqual(self.hashMap.get(1000000), 1000000)

if __name__ == '__main__':
    unittest.main()