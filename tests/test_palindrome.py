import unittest

class TestPalindrome(unittest.TestCase):

    def test_simple1(self):
        result = is_palindrome('oso')
        self.assertEqual(result, True)
    def test_simple2(self):
        result = is_palindrome('ana')
        self.assertEqual(result, True)
    def test_simple3(self):
        result = is_palindrome('level')
        self.assertEqual(result, True)
    def test_simple4(self):
        result = is_palindrome('aa')
        self.assertEqual(result, True)
        
    def test_phrase1(self):
        result = is_palindrome('A man, a plan, a canal: Panama')
        self.assertEqual(result, True)
    def test_phrase2(self):
        result = is_palindrome('Was it a car or a cat I saw?')
        self.assertEqual(result, True)
    def test_phrase3(self):
        result = is_palindrome('No lemon, no melon')
        self.assertEqual(result, True)

    def test_non_palindrome1(self):
        result = is_palindrome('hola')
        self.assertEqual(result, False)
    def test_non_palindrome2(self):
        result = is_palindrome('chau')
        self.assertEqual(result, False)
    def test_non_palindrome3(self):
        result = is_palindrome('el chico juega al futbol')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
