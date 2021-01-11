result = []

def findMissingNumber(arr, size):
    sum = 0
    for i in arr:
        sum += i
    first_n_sum = size*(size+1)//2
    result.append(first_n_sum-sum)

def main():
    n = int(input("No. of test cases: "))
    for A in range(n):
        print("Test case-",A+1)
        arr = list(map(int, input("Enter  elements: ").split()))
        findMissingNumber(arr, len(arr)+1)
    print("\nresults:")
    for i in result:
        print(i)

if __name__ == "__main__":
    main()

#2
def getmissing(a, v):
    x1 = a[0]
    x2 = 1

    for i in range(1, v):
        x1 = x1 ^ a[i]
    for i in range(2, v+2):
        x2 = x2 ^ i
    return x1 ^ x2

if __name__ == "__main__":
    a = [1, 2, 4, 5, 6]
    v = len(a)
    miss = getmissing(a, v)
    print(miss)
