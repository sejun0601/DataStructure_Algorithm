def MergeSort(arr):

    n = len(arr)

    if n == 1:
        return arr
    
    middle = n//2
    l = MergeSort(arr[:middle])
    r = MergeSort(arr[middle:]) 
    
    return merge(l, r)

def merge(l, r):

    merged = []

    while  len(l) != 0 and len(r) != 0 :
        if l[0] < r[0]:
            merged.append(l[0])
            l = l[1:]
        else:
            merged.append(r[0])
            r = r[1:]

    while len(l) != 0 and len(r) ==0:
        merged.append(l[0])
        l = l[1:]

    while len(l) == 0 and len(r) != 0:
        merged.append(r[0])
        r = r[1:]

    return merged


l = [3,4,2,5,6,78,3,5,6,2,1,7]

print(MergeSort(l))

