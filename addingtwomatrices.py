# Program to add two matrices using nested loop
 
a = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
b = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(a)):  
# iterate through columns
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
 
for k in result:
    print(k)