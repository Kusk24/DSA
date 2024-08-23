'''
for i in range(0,n-1):
    if a[i] > a[i+1]:
        a[i], a[i+1], current_lowest = a[i+1], a[i], a[i+1]
        for j in range(1, i):
            current_lowest = a[i]
            if current_lowest < a[j-1]:
                a[j-1], current_lowest = current_lowest, a[j-1]
    else:
         for j in range(1, i):
            current_lowest = a[i]
            if current_lowest < a[j-1]:
                a[j-1], current_lowest = current_lowest, a[j-1]
'''


'''
for i in range(0, n-1):
    e = a[i]
    f = a[i+1]
    if e > f:
        a[i] = f
        a[i+1] = e

    for j in range(1, i):
        g = a[j-1]
        h = a[j]
        if g > h:
            a[j-1] = h
            a[j] = g
'''
 
