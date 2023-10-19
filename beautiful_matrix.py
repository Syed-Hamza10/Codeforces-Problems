matrix = []

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            row, col = i, j

row_dist, col_dist = abs(2 - row), abs(2 - col) 
total_dist = row_dist + col_dist
print(total_dist)


        
    
