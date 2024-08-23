#Name - Win Yu Maung
#ID - 6612054
#Sec - 542

import time
from Heap import heap

testList = list(map(int, input().split()))

start = time.process_time()

number = heap(items=testList)   # default as min heap for a list of numbers


new = []

while not number.empty():
    new.append(number.extract())

def minTotalCost(A):
    total_cost = 0
    min_heap = heap(A, cmp=lambda x, y : x < y)

    while min_heap.heapsize > 1:
        first = min_heap.extract()
        second = min_heap.extract()
        cost = first + second
        total_cost += cost
        min_heap.insert(cost)

        
    return total_cost


cost = minTotalCost(new)

end = time.process_time()

print("\nthe sum of cost is ",cost )
print("\ntime estimated, " , end - start)

