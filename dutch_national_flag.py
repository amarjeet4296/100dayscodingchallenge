

def dutch_national_flag(arr):
    low, high = 0, len(arr) - 1
    i = 0

    while (i <= high):
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else: #arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]

if __name__ == "__main__":
    array = [0,0,2,1,2,2,0,1,2,0,0,1,1,2,2]
    print(dutch_national_flag(array))
    
