#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    swap = True

    while swap:
        swap = False
        for index in range(len(lst)-1):
            if lst[index] > lst[index + 1]:
                swap = True
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 5, 9], [4, 7, 10, 11])
    [1, 3, 4, 5, 7, 9, 10, 11]
    """
    sorted_nums = []

    while len(list1) != 0 or len(list2) != 0:
        if len(list1) == 0:
            sorted_nums.append(list2.pop(0))
        elif len(list2) == 0:
            sorted_nums.append(list1.pop(0))
        elif list1[0] > list2[0]:
            sorted_nums.append(list2.pop(0))
        else:
            sorted_nums.append(list1.pop(0))

    return sorted_nums

##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    this input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) <= 1:
        return lst

    list1 = merge_sort(lst[:len(lst)/2])
    list2 = merge_sort(lst[len(lst)/2:])

    return merge_lists(list1, list2)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
