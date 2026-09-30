import unittest
from validators import is_valid_amount

class TestProject(unittest.TestCase):
    def test_amount(self):
        self.assertTrue(is_valid_amount("100"))
        self.assertFalse(is_valid_amount("-10"))
        self.assertFalse(is_valid_amount("abc"))

if __name__=="__main__":
    unittest.main()
