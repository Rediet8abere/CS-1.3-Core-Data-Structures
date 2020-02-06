#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        # print("self __init__", self)
        self.list = LinkedList()
        self.top = None
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        self.list.append(item)
        self.top = item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.top

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any

        if self.is_empty():
            raise ValueError('Stack is empty')
        self.list.delete(self.top)
        return self.top



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        print("Array self__init__", self)
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)


    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list == []

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        # print("self", self.list)
        # print("type", type(self.list))
        # return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)


    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        # print("self.list[-1]", self.list[-1])
        # return self.list[-1]



    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack(['A', 'B', 'C', 'R'])
# print("Stack.list", Stack.list)
# print("is_empty", Stack.is_empty())
# Stack.pop()
# print(Stack.length())
# print("peek", Stack.peek())
# print("Stack.list", Stack.list)
Stack = ArrayStack(['A', 'B', 'C', 'R'])
print("stack list", Stack.list)
print("pop", Stack.pop())
print("peek", Stack.peek())
print("len", Stack.length())
# print("empty", Stack.is_empty())
