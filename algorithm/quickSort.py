import random
import time

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(more)

listArr = list(range(1, 1000000))
random.shuffle(listArr)
start_time = time.time()
quicksort(listArr)
end_time = time.time()
print(end_time - start_time)