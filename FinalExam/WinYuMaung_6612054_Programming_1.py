#Name - Win Yu Maung,
# ID - 6612054,
# Section-542
class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))  # [0,1,2,3,4,5,6,7,8]
        self.rank = [0] * n  # [0,0,0,0,0,0,0,0,0]

    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

def spread(r,c, matrix):
    s = DisjointSets(r*c)

    #index formula from 2D array to 1D array
    #index = i * c + j
    time = 0

    adj_check = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(r):
        spreading = 0
        for j in range(c):
            if matrix[i][j] == 2:
                index = i * c + j #from 2D array to 1D array index
                for di, dj in adj_check: #right up left down
                    ni, nj = i + di, j + dj #looking right up left down from current location therefore row+di columns+dj
                    if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] == 1: #to ensure within 0 and max rows or columns and also to be 1
                        neighbor_index = ni * c + nj
                        matrix[ni][nj] = 2
                        s.union(index, neighbor_index)
                        spreading += 1

        if spreading >= 0:
            time += 1

    for i in matrix:
        for j in i:
            if j == 1:
                return -1

    return time

r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
print("Answer: ", spread(r, c, matrix))

# .!.