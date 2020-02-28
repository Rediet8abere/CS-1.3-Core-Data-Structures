from set import Set
from hashtable import HashTable
import unittest

class SetTest(unittest.TestCase):
    def test_init(self):
        set = Set()
        assert set.size == 0

    def test_contains(self):
        set = Set(['Master of the Game'])
        assert set.contains('Master of the Game') == True

        set.remove('Master of the Game') #element will be removed from set
        assert set.contains('Master of the Game') == False

    def test_add(self):
        set = Set()
        set.add('After the darkness')
        assert set.size == 1 # added one element

        set.add('Dertogada')
        assert set.size == 2 # added a second element

        set.add('Ramatohara')
        assert set.size == 3 # added a thrid element

        set.add('Ramatohara')
        assert set.size == 3 # element already exist, no size change

    def test_remove(self):
        # Double check
        set = Set(['Talent code', 'Outliers', 'Talking to strangers'])
        set.size == 3 #started with 3 elements

        set.remove('Talent code')
        set.size == 2 #one element is removed

        set.remove('Outliers')
        set.size == 1 #second element removed

        set.remove('Talking to strangers')
        set.size == 0 #third element removed

    def test_union(self):
        # Double check
        set = Set(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
        other_set = Set(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        set.union(other_set.elements) is {'Talent code': 'Talent code', 'Outliers':'Outliers', 'Talking to strangers':'Talking to strangers',
        'Beloved': 'Beloved', 'Nightingale':'Nightingale', 'Mistress of the game':'Mistress of the game'}

if __name__ == '__main__':
    unittest.main()
