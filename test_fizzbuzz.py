import unittest
import fizzbuzz as fb


class FizzBuzzzTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_normal(self):
        self.assertEqual(1, fb.fizzbuzz(1))
        
    def test_fizz(self):
        self.assertEqual("Buzz", fb.fizzbuzz(5))
        
    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fb.fizzbuzz(15))
        
if __name__ == "__main__":
    unittest.main()