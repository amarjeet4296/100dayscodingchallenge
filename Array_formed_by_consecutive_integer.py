def isConsecutive(A):

    minimum = min(A)
    maximum = max(A)


# the maximum and minimum element in it should be exactly `n-1`
    if maximum - minimum != len(A) - 1:
        return False

    # create an empty set
    visited = set()

    for i in A:
        if i in visited:
            return False

        visited.add(i)
    return True


if __name__ == '__main__':

    A = [-1, 5, 4, 2, 0, 3, 1, 6]

    if isConsecutive(A):
        print("The array contains consecutive integers from {0} to {1}".format(min(A), max(A)))
    else:
        print("Array does not contain consecutive integers")
