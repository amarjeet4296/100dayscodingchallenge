def isIsomorphic(X, Y):
    if len(X) != len(Y):
        return False

    dict = {}
    s = set()

    for i in range(len(X)):
        y = X[i]
        x = Y[i]
        if x in dict:
            if dict[x] != y:
                return False
        else:
            if y in s:
                return False
            dict[x] = y
            s.add(y)
    return True

if __name__ == "__main__":
    X = "CVBD"
    Y = "XYZV"

    if isIsomorphic(X, Y):
        print("True")
    else:
        print ("False")
