#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found
        Time-complexity: Best Case: o(1) item could be the first element
                         Worst Case: 0(n) item could be at the middle or end of array """
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
    """return the index of item in sorted array or None if item is not found
    Time-complexity: Best Case: o(1) item could be the middle element
                     Worst Case: 0(log n) after n iterations of reducing the array by half
                     the length of array will be 1  2^i = len(array), i-iterations
                     log 2^i = log n ==> i = log n, n-len(array) therefore we have to iterate log(n) times """


    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(sorted(array), item, 0, len(array)-1)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    array = sorted(array)
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

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left, right):
    # TODO: implement binary search recursively here

    low = left
    high = right
    mid = (low + high) //2
    print("array", array)

    print("low", low)
    print(array[low])
    print("high", high)
    print(array[high])
    print("item", item)
    # 1
    #
    if low > high:
        return None

    if array[mid] > item:
        print("greater")
        high = mid - 1
        mid = (low + high) //2
        return binary_search_recursive(array, item, left=low, right=high)
    elif array[mid] < item:
        print("lessthan")
        low = mid + 1
        mid = (low + high) //2
        return binary_search_recursive(array, item, left=low, right=high)
    elif item == array[mid]:
        return mid

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

def main():
    num = [89, 2, 4, 5, 34, 56, 78, 90, 3]
    result = binary_search(num, 5)
    # result2 = binary_search(num, 2)
    print("result", result)
    # print("result2", result2)




if __name__ == '__main__':
    main()
