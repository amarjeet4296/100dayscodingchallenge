def Isdisjoint(set1, set2, x, y):
    set1.sort()
    set2.sort()
    i = 0; j = 0
    while(i < x, j < y):
        if (set1[i] < set2[j]):
            i += 1
        elif (set2[j] < set1[i]):
            j += 1
        else:
            return False
    return True
if __name__ == "__main__":
    set1 = [23, 4, 5, 78, 45]
    set2 = [1, 2, 3, 4]
    x = len(set1)
    y = len(set2)
    if (Isdisjoint(set1, set2, x, y)):
        print ("Yes")
    else:
        print("No")
