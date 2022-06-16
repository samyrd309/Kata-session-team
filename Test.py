
import unittest
import Main

class TestMainMethods(unittest.TestCase):
    def test_interger_range_contains_1(self):
        range = [2,3,4,5]
        val = [2,4]
        output = Main.integer_range_contains(range, val)
        self.assertTrue(output)

    def test_interger_range_contains_2(self):
        range = [2,3,4,5]
        val = [-1,1,6,10]
        output = Main.integer_range_contains(range, val)
        self.assertFalse(output)
    
    def test_get_all_ppints(self):
        range = [2,3,4,5]
        output = Main.getAllPoint(range)
        self.assertEqual(range,  [2,3,4,5])
        
    def test_ContainsRange_1(self):
        range1 = [2,3,4]
        range2 = [7,8,9]
        output = Main.ContainsRange(range1, range2)
        self.assertFalse(output)
    
if __name__ == '__main__':
    unittest.main()