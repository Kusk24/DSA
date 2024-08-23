#Name - Win Yu Maung
#ID - 6612054
#Section - 542

import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()

# write the insertion sort code into this segment

current_lowest = a[0]


for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key


    
et = time.process_time()

print(a)
print(et-st)

            
