#Name - Win Yu Maung
#ID - 6612054
#Section - 542

K = int(input())
a = list(map(int, input().split()))

import time

st = time.process_time()

def LinearSearch(alist , target):
    for i in alist:
        if i == target:
            return True
        else:
            continue        
        

found = False
for x in a:
    y = K/x
    if y != x:
        found = LinearSearch(a, y)
    if found:
        break



et = time.process_time()

if not found:
    print("No pair can be sumed to K")
else:
    print(x, int(y))

print("time estimation: ", et - st)
    

