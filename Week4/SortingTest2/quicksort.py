#Name - Win Yu Maung
#ID - 6612054
#Sec - 542

import sys
sys.setrecursionlimit(10000)

counter = 0

def partition(A, p, r):  # Lomuto's partition scheme
    global counter
    x = A[r] #pivot
    i = p-1
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

def quicksort( A, low, high): #low and high are index
    if low <= high: #specific criteria
        position = partition(A, low, high)

        #for the left subarray
        quicksort(A, low, position - 1) #in case low is 0 and (position - 1) is -1 then only it will just stop working  without stopping any other quicksort
        #for the right subarray
        quicksort(A, position + 1, high)

'''
#Exercise 2
number = [2,3,8,6,8,4,1]
pivot  = partition(number, 0, len(number)-1)
print("All except minimum")
print("pivot = ", number[pivot], ", numberlist = ", number)
print(f"To print from left side of pivot to right end {number[pivot+1 : ]}")
print(f"To print from right side of pivot to left end {number[ : pivot]}")

number = [2,3,8,6,8,4,1,9]
pivot  = partition(number, 0, len(number)-1)
print("\nAll except maximum")
print("pivot = ", number[pivot], ", numberlist = ", number)
print(f"To print from left side of pivot to right end {number[pivot+1 : ]}")
print(f"To print from right side of pivot to left end {number[ : pivot]}")

number = [2,3,8,6,8,4,1,5]
pivot  = partition(number, 0, len(number)-1)
print("\ntwo halves")
print("pivot = ", number[pivot], ", numberlist = ", number)
print(f"To print from left side of pivot to right end {number[pivot+1 : ]}")
print(f"To print from right side of pivot to left end {number[ : pivot]}")
'''

n = list(map(int,input("Enter your number: ").split()))
quicksort( n, 0, len(n)-1)
print(n)
print("running time as counter: ",counter)
