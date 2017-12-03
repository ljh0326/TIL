#분할정복 예제 

#배열에 있는 숫자 더하기
# 반복문 이용할 경우
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
print(1)
print(sum([1, 2, 3, 4]))

#분할 정복 사용시
#1.기본단계 원소의 개수가 0개거나 1개인 배열을 받으면 합계를 구하는 것은 간단
#2. 호출되는 배열의 크기가 점점 줄어들어야 한다 어떻게?
# sum([2,4,6])은 2 + sum([4,6])과 같다. 즉 더 작은 배열을 넘김


def sum2(arr):
    if len(arr) <= 0:
        return 0
    else:
        return arr[0] + sum2(arr[1:])
print(2)
print(sum2([1, 2, 3, 4]))
