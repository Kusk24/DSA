#Name - Win Yu Maung
#ID - 6612054
#Section - 542

import time

start = time.process_time()

A = list(map(int, input().split()))

n = len(A)

def checkoutMax(a, lastIndex=0):
    # Locate the position of max item
    # Replace the item at max position with the last item
    # Return value of max item
    
    maxIndex = 0
    for i in range(1, lastIndex+1):
        if a[i] > a[maxIndex]:
            maxIndex = i
    maxItem = a[maxIndex]
    a[maxIndex] = a[lastIndex]
    return maxItem

    
for i in range(n-1, -1, -1):
    A[i] = checkoutMax(A, i)


end = time.process_time()
time = end - start
print(A)

print(f"Time estimated is {time}")



