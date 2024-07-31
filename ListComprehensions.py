x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
dimensions = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1)]
sum_dimensions = [dimension for dimension in dimensions if sum(dimension) != n]
print(sum_dimensions)