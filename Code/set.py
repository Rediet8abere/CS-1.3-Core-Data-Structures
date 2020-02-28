from hashtable import HashTable


class Set(object):
    def __init__(self, elements=None):
        """ Initialize a new empty set structure, and add each element
            if a sequence is given. """
        self.elements = HashTable()
        # print(self.elements)
        self.size = 0 # property that tracks the number of elements in constant time
        if elements is not None:
            for item in elements:
                self.add(item)


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
            Running time: O(n^2) we have to traverse
            through self and other_set inorder to the union
            Space (memory): O(n) we have to create a temporary space for the other_set_keys
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        other_set_key = other_set.elements.keys()
        print('other_set_key', other_set_key)
        for ele in other_set_key:
            if not self.contains(ele):
                self.add(ele)
        return self.elements


    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set.
            Running time:  O(n^2) we have to traverse
            through self and other_set inorder to the union
            Space (memory): O(n) we have to create a temporary space for the other_set_keys
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        other_set_key = other_set.elements.keys()
        interset = []
        for ele in other_set_key:
            if self.contains(ele):
                interset.append(ele)
        return Set(interset).elements



    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set.
            Running time:  O(n^2) we have to traverse
            through self and other_set inorder to the union
            Space (memory):O(n) we have to create a temporary space for the other_set_keys
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """

        for ele in self.intersection(other_set).keys():
            self.remove(ele)
        return self.elements


    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set.
            Running time:  O(n^2) we have to traverse through self and other_set inorder to the union
            Space (memory):O(n) we have to create a temporary space for the other_set_keys
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        other_set_key = other_set.elements.keys()
        count = 0
        for ele in other_set_key:
            if self.contains(ele):
                count += 1
        return count == other_set.size
set = Set(['Talent code', 'Outliers', 'Talking to strangers', 'Idea man'])
other_set = Set(['Beloved', 'Nightingale', 'Mistress of the game', 'Idea man'])
# print('union --->', set.union(other_set))
# print('intersection - -->', set.intersection(other_set))
# print('difference ----->', set.difference(other_set))
print('is_subset ----->', set.is_subset(other_set))
