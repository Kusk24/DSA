#Myat Phone Paye
#6530258
#543
def count_pairs_with_condition(n, arr):
        count = 0
        value_map = {}
     
        for i in range(1, n + 1):
            value_i = arr[i - 1] + i**2
            if value_i in value_map:
                value_map[value_i] += 1
            else:
                value_map[value_i] = 1
     
        for j in range(1, n + 1):
            value_j = arr[j - 1] - j**2
            if value_j in value_map:
                count += value_map[value_j]
     
        return count
     
# Read input
n = int(input())
arr = list(map(int, input().split()))
     
# Get the result
result = count_pairs_with_condition(n, arr)
     
# Print the result
print(result)