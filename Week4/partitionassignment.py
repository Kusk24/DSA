
def partition(A, p, r):  # Lomuto's partition scheme
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

def quicksort(A, low, high):
    if (low < high):
        pos = partition(A, low, high)
        print(A[low:pos])
        print(A[pos])
        print(A[pos+1:high+1])
        print("-----------")
        quicksort(A, low, pos-1)
        quicksort(A, pos+1, high)

case1 = [5, 10, 8, 4, 6, 3, 1]
print("\nBefore partition: ")
print(case1)
pos = partition(case1, 0, len(case1)-1)
print("After partition: ")
print(case1)
print("Partition 1: ", case1[:pos])
print("Pivot: ", case1[pos])
print("Partition 2: ", case1[pos+1:])

case3 = [9, 1, 3, 6, 4, 8, 10]
print("\nBefore partition: ")
print(case3)
pos = partition(case3, 0, len(case3)-1)
print("After partition: ")
print(case3)
print("Partition 1: ", case3[:pos])
print("Pivot: ", case3[pos])
print("Partition 2: ", case3[pos+1:])

case3 = [9, 3, 6, 4, 2, 8, 5]
print("\nBefore partition: ")
print(case3)
pos = partition(case3, 0, len(case3)-1)
print("After partition: ")
print(case3)
print("Partition 1: ", case3[:pos])
print("Pivot: ", case3[pos])
print("Partition 2: ", case3[pos+1:])

case4 = [3, 7, 2, 4, 8, 6, 5]
print("\nBefore partition: ")
print(case4)
pos = partition(case4, 0, len(case4)-1)
print("After partition: ")
print(case4)
print("Partition 1: ", case4[:pos])
print("Pivot: ", case4[pos])
print("Partition 2: ", case4[pos+1:])

example = [10, 8, 4, 6, 3, 9]
print("===========")
quicksort(example, 0, len(example)-1)
print(example)

exercise = [29, 18, 4, 30, 12, 50, 9]
print("===========")
quicksort(exercise, 0, len(exercise)-1)
print(exercise)

example2 = [3, 4, 9, 1, 7, 0, 5, 2, 6, 8]
print("===========")
quicksort(example2, 0, len(example2)-1)
print(example2)

# example3 = [5, 4, 1, 6, 3, 7, 2]
example3 = [4, 2, 7, 3, 1, 9, 6, 0, 8]
print("===========")
quicksort(example3, 0, len(example3)-1)
print(example3)
