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

    def __str__(self):
        """Return a formatted string representation of this set."""
        items = ['{!r}'.format(key) for key in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this set."""
        return 'Set({!r})'.format(self.items())


    def contains(self, element):
        """ return a boolean indicating whether element is in this set.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        index = self.elements._bucket_index(element)
        bucket = self.elements.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value == element)
        return entry is not None  # True or False


    def add(self, element):
        """add element to this set, if not present already.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        # Find the bucket the given key belongs in
        index = self.elements._bucket_index(element)
        bucket = self.elements.buckets[index]
        print('bucket', bucket, index, element)
        # # Find the entry with the given key in that bucket, if one exists
        # # Check if an entry with the given key exists in that bucket
        # entry = bucket.find(lambda key_value: key_value[0] == key)
        if not self.contains(element):  # Found
            # Insert the new element into the bucket
            bucket.append(element)
            self.size += 1
        # print('bucket', bucket)

    def items(self):
         return self.elements.items()

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        index = self.elements._bucket_index(element)
        bucket = self.elements.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value == element)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))


    def union(self, other_set):
        """return a new set that is the union of this set and other_set.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
        print(self)
        print(other_set)
        # key_list = other_set.keys()
        # for k in key_list:
        #     print(self.elements.contains(k))
        #     if not self.elements.contains(k):
        #         self.add(k)
        # print("In union", self.elements)
        # return self.elements

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """

        # key_list = other_set.keys()
        # print('key_list', key_list)
        # intersect = []
        # for k in key_list:
        #     if self.elements.contains(k):
        #         intersect.append(k)
        # print('in intersection', intersect)
        # set = Set(intersect)
        # return set.elements

        # return self.elements



    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """

    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set.
            Running time:
            Space (memory):
            Compare the behaviors of your Set class to those of the Python
            set type and Swift Set type:
        """
set = Set(['Becoming', 'Lean In', 'Whistling Vivaldi'])
# print('set', set, set.size)
# print('contains', set.contains('A')) #should return false
# print('contains', set.contains('Becoming')) #should return true
# set.remove('Becoming')
# print('remove', set.size) #should return true
# print('set', set)

# print('adding outliers', set.add('Outliers'))
# print(set.elements)
# print(set.contains('xx'))
# set.remove('Lean In')
other_set = {'Talent code', 'Outliers', 'Talking to strangers'}
set.union(other_set)
print('other_set', other_set)
print('self.size', set.size)

# set = Set(['Nightingale', 'The originals', 'Whistling Vivaldi', 'Becoming', 'Lean In'])
# print("sesond set", set.elements)
#
# print("merging", set.union(other_set))
# print('intersexting', set.intersection(other_set))
