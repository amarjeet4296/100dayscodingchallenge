def customSort(first, second):

    # dictionary to store the frequency of each element of the first list
    freq = {}

    # find the frequency of each element of the first list and
    # store it in a dictionary.
    for i in first:
        freq[i] = freq.get(i, 0) + 1

    # Note that once we have the frequencies of all elements of
    # the first list, we can overwrite elements of the first list

    index = 0

    # do for every element of the second list
    for i in second:

        # If the current element is present in the dictionary, print it `n` times
        # where `n` is the frequency of that element in the first list
        n = freq.setdefault(i, 0)
        for _ in range(n):
            first[index] = i
            index = index + 1

        # erase the element from the dictionary
        freq.pop(i)

    # Now we are left with elements only present in the first list
    # but not in the second list.

    # sort the remaining elements present on the dictionary
    for key in sorted(freq.keys()):
        count = freq.get(key)
        while count:
            first[index] = key
            count = count - 1
            index = index + 1


if __name__ == '__main__':

    first = [5, 8, 9, 3, 5, 7, 1, 3, 5, 5, 9, 3, 5, 1, 8, 4]
    second = [3, 5, 7, 2]

    customSort(first, second)
    print("After sorting the list is:", first)
