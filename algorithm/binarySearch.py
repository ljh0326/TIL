
def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    #가장 낮은 수가 높은 수와 같거나 넘어가면 찾는 숫자가 없음
    while low <= high:
        
        # 1. 중간을 계산한다.
        mid = (low + high) // 2
        # 2. 중간값 가져와서
        guess = list[mid]

        # 3. 중간 값이 찾는 값과 같다면 MID반환
        if guess == item:
            return mid
        # 4. 중간값이 찾는 값보다 더 작다면 low를 올린다.
        if guess < item:
            low = mid + 1
        # 5. 중간값이 찾는값보다 더 크다면 high를 낼니다.
        if guess > item:
            high = mid - 1

    #none는 아무것도 아니라는 뜻
    return None

myList = [1, 3, 5, 7, 9]

print(binarySearch(myList, 3))
print(binarySearch(myList, -1))