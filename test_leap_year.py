import unittest
import datetime
from leap_year import isleap, days, get_weekday


class DaysTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_isleap(self):
        self.assertTrue(isleap(2024))
        
    def test_weekday(self):
        dt = datetime.datetime(2024, 3, 18)
        # print(dt.strftime('%a'))
        self.assertEqual(get_weekday(2024, 3, 18), dt.strftime('%a'))
                         
    
if __name__ == "__main__":
    unittest.main()