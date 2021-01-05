def bsearch(a, item):
    beg = 0
    last = len(a) -1
    while(beg <= last):
        mid = int((beg + last)/2)
        if(item == a[mid]):
            return mid
        elif(item > a[mid]):
            beg = mid + 1
        else:
            last = mid - 1
    else:
        return false
n = int(input("Enter size of array or list"))
print("Enter number in ascending order")
a = []
for i in range(n):
    i = int(input("Enter Number in pocket [ "+str(i)+"]"))
    a.append(i)
item = int(input("Enter Search item"))
index = bsearch(a, item)
if index:
    print("Element found in", index + 1)
else:
    print("Not found")
