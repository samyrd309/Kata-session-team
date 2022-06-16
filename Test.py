
import unittest
import Main

class TestMainMethods(unittest.TestCase):
    def test_interger_range_contains_1(self):
        range = [2,3,4,5]
        val = [2,4]
        output = Main.integer_range_contains(range, val)
        self.assertTrue(output)
        
    
    
if __name__ == '__main__':
    unittest.main()