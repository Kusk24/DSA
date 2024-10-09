#Name - Win Yu Maung, ID - 6612064, Sec 542

from disjointsets3 import DisjointSets

def largest_cloud(r, c, image):
    s = DisjointSets(r * c)

    cloudSize = {}

    for i in range(r):
        for j in range(c):
            if image[i][j] == 1:
                index = i * c + j

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and image[ni][nj] == 1:
                        neighbor_index = ni * c + nj
                        s.union(index, neighbor_index)

    for i in range(r):
        for j in range(c):
            if image[i][j] == 1:
                root = s.findset(i * c + j)
                if root in cloudSize:
                    cloudSize[root] += 1
                else:
                    cloudSize[root] = 1

    return max(cloudSize.values()) if cloudSize else 0  # Handle empty case


r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
print("Answer: ", largest_cloud(r, c, matrix))