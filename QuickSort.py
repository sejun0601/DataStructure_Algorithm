def quickSort(array) -> list:
    s = 0
    e = len(array)-1
    pivot = len(array)//2

    if len(array) == 1:
        return array

    while s<e:
        if array[s] >= array[pivot] and array[e]<= array[pivot]:
            array[s], array[e] = array[e], array[s]
            s += 1
            e -= 1

        elif array[s] >= array[pivot] and not array[e]<= array[pivot]:
            e -= 1
        elif not array[s] >=array[pivot] and array[e]<= array[pivot]:
            s += 1
        else:
            s += 1
            e -= 1
    llist = array[0:s]
    rlist = array[s:]

    return quickSort(llist) + quickSort(rlist)

l = [5,7,8,9,6,4,3,2,0,1,3,5,8,8,43,23,34,6,6,6,8,9,3,45,34,664]
print(quickSort(l))

def quick_sort2(arr):
    # 리스트가 하나 이하의 요소를 가지면 이미 정렬된 것으로 간주
    if len(arr) <= 1:
        return arr
    
    # 피벗 선택 (여기서는 리스트의 중간 요소를 피벗으로 선택)
    pivot = arr[len(arr) // 2]
    
    # 피벗을 기준으로 리스트를 분할
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 재귀적으로 분할된 리스트들을 정렬하고 병합
    return quick_sort2(left) + middle + quick_sort2(right)

# 사용 예시
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort2(arr)
print("Sorted array:", sorted_arr)


def quick_sort3(arr,l,r):

    if l < r:
        p = partition(arr,l,r)
        quick_sort3(arr, 0, p-1)
        quick_sort3(arr,p+1, r)

def partition(arr, l,r) -> int:
    pivot = arr[r]

    i = l-1
    for j in range(l,r):
        if arr[j] <pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i+1] = arr[i+1], arr[r]

    return i+1

quick_sort3(arr, 0, len(arr)-1)
print(arr)
    