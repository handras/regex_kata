import unittest
from regex_kata.regex import regex


class test_re(unittest.TestCase):
    reg = regex()

    def test1(self):
        self.assertTrue(self.reg.match('aba', 'aba'))
        self.assertTrue(self.reg.match('abaaa', 'abaaa'))
        self.assertFalse(self.reg.match('ab', 'aba'))
        self.assertFalse(self.reg.match('ba', 'ab'))
        self.assertFalse(self.reg.match('abab', 'aba'))

    def test2(self):
        self.assertTrue(self.reg.match('a', 'a*'))
        self.assertTrue(self.reg.match('aaab', 'a*b'))
        self.assertTrue(self.reg.match('aaab', 'a*b*'))
        self.assertTrue(self.reg.match('bbaaa', 'a*b*a*'))
        self.assertFalse(self.reg.match('abbaaa', 'aba*'))

    def test3(self):
        self.assertTrue(self.reg.match('a', '.'))
        self.assertTrue(self.reg.match('b', '.'))
        self.assertTrue(self.reg.match('aaab', 'a..b'))
        self.assertTrue(self.reg.match('abab', 'a..b'))
        self.assertFalse(self.reg.match('abbaaa', 'b..a'))
        self.assertFalse(self.reg.match('', 'b..a'))

    def test4(self):
        self.assertTrue(self.reg.match('', '.*'))
        self.assertTrue(self.reg.match('', '.*.*'))
        self.assertTrue(self.reg.match('a', '.*'))
        self.assertTrue(self.reg.match('bbb', '.*'))
        self.assertTrue(self.reg.match('aaab', '.*'))
        self.assertTrue(self.reg.match('abab', 'a.*.b'))
        self.assertFalse(self.reg.match('abbaaab', 'b..a*'))
        self.assertFalse(self.reg.match('', 'b..a'))

    def test5(self):
        self.assertTrue(self.reg.match('', '.?'))
        self.assertTrue(self.reg.match('a', '.?'))
        self.assertTrue(self.reg.match('bb', '..?'))
        self.assertTrue(self.reg.match('ab', 'a?b?'))
        self.assertTrue(self.reg.match('bbb', 'a?bbb?b?'))


if __name__ == '__main__':
    unittest.main()
