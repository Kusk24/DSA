def partition(A, p, r):  # Lomuto's partition scheme
    x = A[r] #pivot
    i = p-1
    print(f"i is {i}")
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            print(f"step under for loop {A[i]},{A[j]} = {A[j]},{A[i]}")
            A[i],A[j] = A[j],A[i]
    print(f"outside step {A[r]},{A[i+1]} = {A[i+1]},{A[r]}")
    A[r],A[i+1] = A[i+1],A[r]
    return i+1


number = [8, 6, 5, 3, 2, 1]
partition(number, 0, len(number)-1)


'''
number = [8, 6, 5, 3, 2, 1]
p = partition(number,0, len(number)-1) #index of pivot


# underneath p will be printed exclusively

print(number[p])
print(number[:p]) #p is exclusive because right side of : is exclusive
print(number[p+1:])
'''
