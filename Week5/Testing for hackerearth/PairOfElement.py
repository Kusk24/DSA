#Name - Win Yu Maung
#ID - 6612054
#Sec - 542


n = int(input())
arr = list(map(int, input().split()))


#arr[j] - arr[i] = (i+1)**2 + (j+1)**2
#arr[j] - (j+1)**2 = arr[i] + (i+1)**2

array = {}
array2 = {}

#L.H.S
for i in range(0, n):
    a = (arr[i] + (i+1)**2)
    if a not in array:
        array[a] = 1
    else:
        array[a] += 1

#R.H.S
for j in range(0, n):
    b = (arr[j] - (j+1)**2)
    if b not in array2:
        array2[b] = 1
    else:
        array2[b] += 1


count = 0

for key,value in array.items():
    if key in array2:
        if array[key] < array2[key]:
            count += array2[key]
        else:
            count += array[key]
        
print(count)
