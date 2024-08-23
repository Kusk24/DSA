#Name - Win Yu Maung
#ID - 6612054
#Section - 542

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = A[p + i]
    for j in range(n2):
        right[j] = A[q + 1 + j]


    i = 0  
    j = 0  
    k = p  

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1
        
    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1



def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)
        


a = list(map(int, input().split()))

import time

st = time.process_time()
mergesort(a, 0, len(a) - 1)
et = time.process_time()

print(a)
print(et - st)

