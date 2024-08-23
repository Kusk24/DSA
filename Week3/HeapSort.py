#Name - Win Yu Maung
#ID - 6612054
#Sec - 542

import time
from Heap import heap

def myCompare(x, y):   # max heap
    return x.key > y.key


class myClass:
    def __init__(self, k):
        self.key = k
        

testList = list(map(int, input().split()))

start = time.process_time()

pq = heap(cmp=myCompare)  # custom class item with custom compare function

for v in testList:
    pq.insert(myClass(v))

while not pq.empty():
    print(pq.extract().key, end=' ')

end = time.process_time()

print("\ntime estimated ", end - start)
