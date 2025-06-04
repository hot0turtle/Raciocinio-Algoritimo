# pegar somente as colunas

 
mat = [[2,1], [5,1]]
matxy = 2

mat2 = [[2,1,3,5,9], [5,1,1,2,9], [1,2,3,4,5]]
mat2y = 3
mat2x = 5

mat3 = [[2,1,3,5,9,17,23,98,2,14], 
        [5,1,1,2,9,432,32,3,4,5], 
        [1,2,3,4,5,6,7,8,9,0], 
        [5,1,1,2,9,431,32,3,4,5], 
        [1,2,3,4,5,6,7,8,9,0]]
mat3x = 10
mat3y = 5

soma = 0

for a in range(mat2y):
    soma += (mat2[a][0])

print(soma)
c= 0
biggest = mat3[0][0]
for j in range(mat3y):
    if mat3[j][c] > biggest:
        biggest = mat3[j][c]
    for c in range(mat3x):
        if mat3[j][c] > biggest:
            biggest = mat3[j][c]

print(biggest)


#diagonal média

med = 0
for i in range(mat3y):
    med += mat3[i][i]

med /= mat3y

print(med)