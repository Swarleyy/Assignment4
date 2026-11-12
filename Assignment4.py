
#Matrix addition using array
matrix1=[
[1,2,3],
[4,5,6]
]
matrix2=[
[7,8,9],
[10,11,12]
]
result=[
[0,0,0],
[0,0,0]
]
for i in range(len(matrix1)):
for j in range(len(matrix2)):
result[i][j]=matrix1[i][j]+matrix2[i][j]
print("Matrix 1:")
for row in matrix1 :
print(row)
print("Matrix 2:")
for row in matrix2 :
print(row)
print("\nSum of Matrix 1 and Matrix 2:")
for row in result:
print(row)
