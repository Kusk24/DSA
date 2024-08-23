

import time
from Heap import heap

testList = list(map(int, input().split()))

start = time.process_time()

number = heap(items=testList)   # default as min heap for a list of numbers


new = []

while not number.empty():
    new.append(number.extract())

rope = [0]

print(new)
sum = 0

for i in range(0, len(new) - 1):
    if i == 0:
        tempsum = new[i] + new [i+1]
        rope.append(tempsum)
        sum += rope[i]
    else: 
        tempsum = rope[i] + new[i+1]
        rope.append(tempsum)
        temp = rope[i-1]+tempsum
        sum += rope[i]

sum += rope[-1]
'''
sum = 0
for i in range(len(rope)-1):
    sum += rope[i+1]

    print(sum)
'''    
end = time.process_time()

print(rope)
print(sum)
print("\nthe sum of cost is ", sum )
print("\ntime estimated, " , end - start)
