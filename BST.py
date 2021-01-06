def numberofBST(n):
    N = [0] * (n + 1)
    N[0], N[1] = 1, 1

    for i in range(2, n+1):
        for j in range(1, i + 1):
            N[i] = N[i] + (N[i - j] * N[j - 1])
    return N[n]

if __name__=="__main__":
    n = 5
    print("Number of Unique BST with", n, "keys are:", numberofBST(n))
