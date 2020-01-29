#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if item == array[index]:
        return index
    else:
        return linear_search_iterative(array, item)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # print(len(str(bin(100))[2:]))

    # 6 34 9
    array = sorted(array)
    print("array Sorted", array)
    low = 0
    high = len(array)-1
    mid = (low + high) //2
    for i in range(len(array)):
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            high = mid - 1
            mid = (low + high) //2
        elif array[mid] < item:
            low = mid + 1
            mid = (low + high) //2


    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

def main():
    num = [89, 2]
    result = binary_search(num, 89)
    # result2 = binary_search(num, 2)
    print("result", result)
    # print("result2", result2)




if __name__ == '__main__':
    main()
