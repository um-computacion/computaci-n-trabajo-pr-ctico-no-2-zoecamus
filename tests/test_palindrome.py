import unittest

class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        result = is_palindrome('oso')
        self.assertEqual(result, True)

    def test_simple(self):
        result = is_palindrome('ana')
        self.assertEqual(result, True)

    def test_simple(self):
        result = is_palindrome('level')
        self.assertEqual(result, True)

    def test_a(self):
        result = is_palindrome('aa')
        self.assertEqual(result, True)
    
    def test_ab(self):
        result = is_palindrome('ab')
        self.assertEqual(result, False)  

    def test_aCa(self):
        result = is_palindrome('aCa')
        self.assertEqual(result, True)
