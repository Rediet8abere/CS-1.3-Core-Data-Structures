from hashtable import HashTable
# comment your code

class HashSet(object):
    def __init__(self, elements=None):
        """ Initialize a new empty set structure, and add each element
            if a sequence is given. """
        self.elements = HashTable()
        # print(self.elements)
        self.size = 0 # property that tracks the number of elements in constant time
        if elements is not None:
            for item in elements:
                self.add(item)

    def __repr__(self):
        """Return a string representation of this set."""
        return 'Set({!r})'.format(self.items())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}'.format(element) for element in self.items()]
        return '{' + ', '.join(items) + '}'


    def contains(self, element):
        """ return a boolean indicating whether element is in this set.
            Running time: O(1) assumming the hashtable's load_factor is't too high
            if load_factor is too high O(n)
            Space (memory):  O(n) as the number of element grows, the memory should grow linearly
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        return self.elements.contains(element)

    def add(self, element):
        """add element to this set, if not present already.
            Running time: O(1) assumming the hashtable's load_factor is't too high
            if load_factor is too high O(n)
            Space (memory): O(n) as the number of element grows, the memory should grow linearly
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        if not self.contains(element):
            self.elements.set(element, None)
            self.size += 1

    def items(self):
         return self.elements.keys()

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError.
            Running time: O(1) assumming the hashtable's load_factor is't too high
            if load_factor is too high O(n)
            Space (memory): O(n) as the number of element grows, the memory should grow linearly
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        self.elements.delete(element)
        print("self.elements", self.elements)
        self.size -= 1


    def union(self, other_set):
        """return a new set that is the union of this set and other_set.
            Running time: O(n) we have to loop through other_set
            Space (memory): O(n) we have to create a temporary space for the other_set_keys
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        other_set_key = other_set.elements.keys()
        unite = HashSet(self.elements.keys())
        for ele in other_set_key:
            if not self.contains(ele):
                unite.add(ele)
        return unite


    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set.
            Running time:  O(n) we have to loop other_set inorder to the union
            Space (memory): O(n) we have to create a space for the set that holds
            the intersection items
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        other_set_key = other_set.elements.keys()
        intersect = HashSet()
        for ele in other_set_key:
            if self.contains(ele):
                intersect.add(ele)
        print('intersect', intersect)
        return intersect



    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set.
            Running time:  O(n) we have to loop through self
            Space (memory): O(n) we have to create a temporary space for the new set that
            holds the difference
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        differ = HashSet()
        print('self', self)
        print('other_set', other_set)
        for ele in self.items():
            if not other_set.contains(ele):
                differ.add(ele)
        # print('differ', type(differ))
        #     self.remove(ele)
        return differ


    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set.
            Running time:  O(n) we have to loop through other_set
            Space (memory): O(1) we have to create a space for the count only
        """
        if other_set.size > self.size:
            return False
        other_set_key = other_set.elements.keys()
        count = 0
        for ele in other_set_key:
            if self.contains(ele):
                count += 1
        return count == other_set.size

set = HashSet(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
other_set = HashSet(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man', 'laland'])
set.add('Hello')
print('set', set)
print("#", str(set))
# print("items: ", set.items())
# print('union --->', set.union(other_set).items())
# print('intersection - -->', set.intersection(other_set))
# print('difference ----->', set.difference(other_set))
print('is_subset ----->', set.is_subset(other_set))
