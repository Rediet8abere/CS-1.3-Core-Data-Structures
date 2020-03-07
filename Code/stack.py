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
        # self.top = self.list.head
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
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? we don't have to traverse or loop to append"""
        # TODO: Push given item
        self.list.prepend(item)
        print('self.list', self.list)
        # self.top = item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        print('self.is_empty()', self.is_empty())
        if self.is_empty():
            return None
        print('self.top', self.list.head.data)
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? we don't have to traverse or loop to remove the first item"""
        # TODO: Remove and return top item, if any
        del_top = None
        if self.is_empty():
            raise ValueError('Stack is empty')
        del_top = self.list.head.data
        self.list.delete(self.list.head.data)

        # if self.length()-1 >= 0:
        #     self.top = self.list.get_at_index(self.length()-1)
        return del_top



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        print("iterable", iterable)
        print("self.list", self.list)
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
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? we can find the index from the length"""
        # TODO: Insert given item
        print("item", item)
        self.list.append(item)


    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        print("self.list P", self.list)
        print("length", self.length())
        if self.is_empty():
            return None
        else:
            return self.list[self.length()-1]
        # do n-1
        # return self.list[-]



    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests

Stack = LinkedStack
# ['a', 'b', 's', 'e']
# Stack = ArrayStack
# print(Stack, 'Stack')
# Stack.push('E')
# print(Stack, 'Stack')
# print("peek E", Stack.peek())
# print("stack list", Stack.list)
# print("type", type(Stack.list))
# print("pop", Stack.pop())
#

# print("len", Stack.length())
# print("empty", Stack.is_empty())
