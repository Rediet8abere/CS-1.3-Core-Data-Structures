from set import HashSet
import unittest

class SetTest(unittest.TestCase):
    def test_init(self):
        set = HashSet()
        assert set.size == 0

    def test_contains(self):
        set = HashSet(['Master of the Game', 'After the darkness'])
        assert set.contains('Master of the Game') == True
        assert set.contains('After the darkness') == True
        assert set.contains('Dertogada') == False


    def test_add(self):
        set = HashSet()
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
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers'])
        assert set.size == 3 #started with 3 elements

        set.remove('Talent code')
        assert set.size == 2 #one element is removed

        set.remove('Outliers')
        assert set.size == 1 #second element removed

        set.remove('Talking to strangers')
        assert set.size == 0 #third element removed

    def test_union(self):
        # two sets with one common element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.union(other_set).size == 7

        # two sets with no common ele
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.union(other_set).size == 8


        # two sets with the same element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])

        assert set.union(other_set).size == 4

    def test_intersection(self):
        # two sets with one common element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.intersection(other_set).size == 1

        # two sets with no common ele
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.intersection(other_set).size == 0


        # two sets with the same element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])

        assert set.intersection(other_set).size == 4

    def test_difference(self):
        # two sets with one common element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.difference(other_set).size == 3


        # two sets with no common ele
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.difference(other_set).size == 4


        # two sets with the same element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])

        assert set.difference(other_set).size == 0
    #
    def test_is_subset(self):
        # two sets with one common element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.is_subset(other_set) is False #all the ele in set are not in other_set
        # therefore expecting false

        # two sets with no common ele
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])

        assert set.is_subset(other_set) is False


        # two sets with the same element
        set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])
        other_set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Capital'])

        assert set.is_subset(other_set) is True

if __name__ == '__main__':
    unittest.main()
