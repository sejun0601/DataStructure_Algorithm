def sequential_search(arr, target):
    """
    배열에서 목표 값을 찾기 위해 순차 탐색을 수행합니다.
    
    :param arr: 탐색할 배열
    :param target: 찾고자 하는 값
    :return: 목표 값의 인덱스 (없으면 -1 반환)
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# 사용 예시
arr = [4, 2, 3, 1, 5, 7, 6]
target = 5
result = sequential_search(arr, target)
print(f"Element found at index: {result}")  # 출력: Element found at index: 4

# 존재하지 않는 값 검색
target = 10
result = sequential_search(arr, target)
print(f"Element found at index: {result}")  # 출력: Element found at index: -1
