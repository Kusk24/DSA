K = int(input())
a = list(map(int, input().split()))

import time

st = time.process_time()

found = False
for x in a:
    y = K/x # K = xy , to find 2 numbers mulitplication is equal to K
    if y != x and y in a:
        found = True
        break

et = time.process_time()

if not found:
    print("no pair exists")
else:
    print(x, int(y))
print("running time:", et-st)

