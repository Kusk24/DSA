from disjointsets3 import DisjointSets

def largest_cloud(r,c, matrix):
    s = DisjointSets(r*c)

    #index formula from 2D array to 1D array
    #index = i * c + j
    cloudSize = {}

    adj_check = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                index = i * c + j #from 2D array to 1D array index

                for di, dj in adj_check: #right up left down
                    ni, nj = i + di, j + dj #looking right up left down from current location therefore row+di columns+dj
                    if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] == 1: #to ensure within 0 and max rows or columns and also to be 1
                        neighbor_index = ni * c + nj
                        s.union(index, neighbor_index)

    for i in s.p: #storing cloud to corresponding parent cloud
        if i not in cloudSize:
            cloudSize[i] = 1
        else:
            cloudSize[i] += 1

    maxCloud = 0
    for keys,values in cloudSize.items(): #finding maximum cloud size
        if values > maxCloud:
            maxCloud = values

    return maxCloud


r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
print("Answer: ", largest_cloud(r, c, matrix))