#!python

from linkedlist import LinkedList
# export PYTHONHASHSEED=0

class HashTable(object):

    def __init__(self, init_size=2):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: Worst case is O(n) under what conditions? we have to loop through the object n times"""
        # TODO: Calculate load factor
        # sum = 0
        # for i in range(len(self.buckets)):
        #     sum += self.buckets[i].size
        # return sum/len(self.buckets)
        return self.size/(len(self.buckets))


    def keys(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: WorstCase --> O(n^2)
        under what conditions? we have to loop through the bucket
        and loop through key-value pair to append all values"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: WorstCase --> O(n^2) under what conditions? we have to loop through the bucket
        and loop through key-value pair to append all values"""
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: BestCase --> O(n) if our key-value pair is stored in the head node
        WrostCase --> O(n^2) under what conditions? we have to loop through all buckets n times and traverse through
        the linked list until we get to None """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: WorstCase O(n^2) under what conditions? we have to loop through the list of
        buckets and traverse through linked list to get the length of buckets. """
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets:
            item_count += bucket.length()
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: O(1) under what conditions? If key is in headNode or near headNode
        Worst case running time: O(n) under what conditions? If key is in the middle or the end of linkedlist """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) under what conditions? If key is in headNode or near headNode
        Worst case running time: O(n) under what conditions? If key is in the middle or the end of linkedlist """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: O(1) under what conditions? If key is in headNode or near headNode
        Worst case running time: O(n) under what conditions? If key is in the middle or the end of linkedlist """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            self.size -= 1
            bucket.delete(entry)
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        self.size += 1

        # TODO: Check if the load factor exceeds a threshold such as 0.75
        print('self.load_factor()', self.size, (len(self.buckets)), self.load_factor(), key, value)
        if self.load_factor() > 0.75:
            new_size = self._resize()

        # TODO: If so, automatically resize to reduce the load factor
        # ...

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1) under what conditions? if item is in head node or near head node
        Worst case running time: O(n) under what conditions? if we have to traverse through nodes to find the item [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(n) under what conditions? if the
        entries are chained in the same linkedlist
        Best and worst case space usage: O(n) what uses this memory? we have
        to create n space in memory to store the key value entrires"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # TODO: Get a list to temporarily hold all current key-value entries
        old_bucket = []
        # go through the bucket
        for i in range(len(self.buckets)):
            # print("bucket[i]", self.buckets[i])
            # go through the linkedlist and get all entrires and store it in old_bucket
            for j in range(self.buckets[i].size):
                # print("getting index", self.buckets[i].get_at_index(j))
                old_bucket.append(self.buckets[i].get_at_index(j))
        # TODO: Create a new list of new_size total empty linked list buckets
        # print("old_bucket", old_bucket)
        self.buckets = [LinkedList() for i in range(new_size)]
        # pass the key value pair to set so that the key can be rehashed and assign to a new index
        for i in range(len(old_bucket)):
            self.size -= 1
            self.set(old_bucket[i][0], old_bucket[i][1])

        # TODO: Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size




def test_hash_table():
    ht = HashTable()
    print('HashTable: ' + str(ht))
    print('ht.size', ht.size)
    print("length", len(ht.buckets))
    print('Setting entries:')
    ht.set('I', 1)
    # print('set(I, 1): ' + str(ht))
    print('load_factor', ht.load_factor())
    print('ht.size', ht.size)
    print("length", len(ht.buckets))
    print('------------------------')
    ht.set('V', 5)
    print('ht.size', ht.size)
    print('load_factor', ht.load_factor())
    print("length", len(ht.buckets))
    # print('load_factor', ht.load_factor())
    # print('set(V, 5): ' + str(ht))
    # print('size: ' + str(ht.size))
    # print('length: ' + str(ht.length()))
    # print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))
    # ht.set('X', 10)
    # print('set(X, 10): ' + str(ht))
    # print('load_factor: ' + str(ht.load_factor()))
    # ht.set('L', 50)  # Should trigger resize
    # print('set(L, 50): ' + str(ht))
    # print('load_factor: ' + str(ht.load_factor()))
    # print('size: ' + str(ht.size))
    # print('length: ' + str(ht.length()))
    # print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))
    # print(str(ht))

    # print('Getting entries:')
    # print('get(I): ' + str(ht.get('I')))
    # print('get(V): ' + str(ht.get('V')))
    # print('get(X): ' + str(ht.get('X')))
    # print('get(L): ' + str(ht.get('L')))
    # print('contains(X): ' + str(ht.contains('X')))
    # print('contains(Z): ' + str(ht.contains('Z')))

    # print('Deleting entries:')
    # ht.delete('I')
    # print('delete(I): ' + str(ht))
    # ht.delete('V')
    # print('delete(V): ' + str(ht))
    # ht.delete('X')
    # print('delete(X): ' + str(ht))
    # ht.delete('L')
    # print('delete(L): ' + str(ht))
    # print('contains(X): ' + str(ht.contains('X')))
    # print('size: ' + str(ht.size))
    # print('length: ' + str(ht.length()))
    # print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
