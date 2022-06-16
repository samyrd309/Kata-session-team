
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

    def test_ContainsRange_2(self):
        range1 = [2,3,4]
        range2 = [3,4,5,6,7,8,9]
        output = Main.ContainsRange(range1, range2)
        self.assertFalse(output)
        
    def test_ContainsRange_3(self):
        range1 = [3,4]
        range2 = [2,3,4,5,6,7,8,9]
        output = Main.ContainsRange(range1, range2)
        self.assertFalse(output)
        
    def test_ContainsRange_4(self):
        range1 = [2,3,4,5,6,7,8,9]
        range2 = [3,4,5]
        output = Main.ContainsRange(range1, range2)
        self.assertTrue(output)

    def test_ContainsRange_5(self):
        range1 = [3,4,5]
        range2 = [3,4]
        output = Main.ContainsRange(range1, range2)
        self.assertTrue(output)
    def test_endPoint_1(self):
        range = [2,3,4,5]
        output = Main.endPoints(range)
        self.assertEqual(output, [2,5])
        
    def test_endPoint_2(self):
        range = [2,3,4,5,6]
        output = Main.endPoints(range)
        self.assertEqual(output, [2,6])
        
    def test_endPoint_3(self):
        range = [3,4,5]
        output = Main.endPoints(range)
        self.assertEqual(output, [3,5])

    def test_endPoint_4(self):
        range = [3,4,5,6]
        output = Main.endPoints(range)
        self.assertEqual(output, [3,6])
    
    def test_Equals_1(self):
        range1 = [3,4]
        range2 = [3,4]
        output =  Main.Equals(range1, range2)
        self.assertTrue(output)

    def test_Equals_2(self):
        range1 = [2,3,4,5,6,7,8,9]
        range2 = [3,4]
        output =  Main.Equals(range1, range2)
        self.assertFalse(output)

    def test_Equals_3(self):
        range1 = [2,3,4]
        range2 = [3,4,5,6,7,8,9]
        output =  Main.Equals(range1, range2)
        self.assertFalse(output)
    
    def test_Equals_4(self):
        range1 = [3,4]
        range2 = [2,3,4,5,6,7,8,9]
        output =  Main.Equals(range1, range2)
        self.assertFalse(output)
        
if __name__ == '__main__':
    unittest.main()