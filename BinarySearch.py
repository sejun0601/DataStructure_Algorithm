def binarySearch(arr, target, l ,r):
    
    n = len(arr)
    middle = (l+r)//2

    if n==0:
        return -1

    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binarySearch(arr, target, middle+1,r)
    else:
        return binarySearch(arr, target, l , middle)

l = [1,2,3,4,5,6,7,8,9]
print(binarySearch(l, 9,0, len(l)-1))