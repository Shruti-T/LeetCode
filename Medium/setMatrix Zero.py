# Problem Statement: Given a matrix if an element in the matrix is 0 
# then you will have to set its entire column and row to 0 and then return the matrix.

# -----------------------------------SOLUTION-------------------------------

arr=[[1,1,1],[1,0,1],[1,1,1]]
ij=[]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j]==0):
            ij.append([i,j])

for k in ij:
    for row in range(len(arr[0])):
        arr[k[0]][row]=0
    for col in range(len(arr)):
        arr[col][k[1]]=0

print(arr)