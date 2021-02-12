def majorityElement(A):
    dict = {}
    for i in A:
        dict[i] = dict.get(i, 0) + 1
    for key, value in dict.items():
        if value > len(A)/2:
            return key
    return -1

if __name__ == '__main__':
    A = [3, 8, 5, 1, 1, 1, 1, 1, 1, 1]
    res = majorityElement(A)
    if res != -1:
        print("Yes", res)
    else:
        print("No")
