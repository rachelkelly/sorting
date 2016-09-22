import unittest

# from sort-name import funcs
from bubble import bubble
#from merge import merge

class SortingTests(unittest.TestCase):
    
    def test_2(self):
        self.assertEqual([1, 2], bubble('21'))
        #self.assertEqual('12', merge('21'))

    def test_8(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], bubble('63752841'))
        #self.assertEqual('12345678', merge('63752841'))

    def test_odd(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], bubble('639752841'))
        #self.assertEqual([], merge(''))

    def test_repeat(self):
        self.assertEqual([1, 1, 1, 1], bubble('1111'))
        #self.assertEqual('1111', merge('1111'))

if __name__ == '__main__':
    unittest.main()

