def insertionSort(arr):
    n =  len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [5,4,2,6,7,3,5,8,10]
insertionSort(arr)
print(arr)
