#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.head == None

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? we can access the last node
        without traversing the linkedlist using the tail node"""
        # TODO: Insert given item
        print("enqueueing", self.list)
        self.list.append(item)
        print("enqueueing", self.list)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? No need to traverse to get the head node"""
        # TODO: Remove and return front item, if any
        head_del = None
        if self.is_empty():
            raise ValueError('LinkedList is empty')
        else:
            head_del = self.list.head.data
            self.list.delete(self.list.head.data)
            return head_del


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list == []

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? we can access the last index
        using the length of the array, no need to loop through the list
        """
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            None
        else:
            return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? we use index to retrive the first item from the list"""
        # Remove and return front item, if any
        list_del = None
        if self.is_empty():
            raise ValueError("Item is empty")
        else:
            list_del = self.list[0]
            del self.list[0]
            return list_del


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
q = Queue(['A', 'B', 'C', 'D'])
q.enqueue('E')
print("length", q.length())
print("front", q.front())
print("delete head", q.dequeue())
print("list", q.list)
print("front", q.front())
print("is empty", q.is_empty())
# Queue = ArrayQueue
