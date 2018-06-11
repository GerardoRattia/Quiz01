# Quiz01
#Math 4330 - Quiz 01
# matVec multiplies a matrix and a vector.

def matVec(matrix,vector):
    '''This function takes a matrix and a vector as it's arguments. It then updates each element of the vector by multiplying it by the matrix before returning the now updated vector.
    '''
    result = []

    for i in range(len(matrix)):
        total = 0
        for j in range(len(vector)):
        #this is the function for the matrix*vector multiplication Ax=b.
           total += matrix[i][j] * vector[j]
        result.append(total)

    return result
# 3x3 matrix
matrix = [[12,7,3],
         [4 ,5,6],
         [7 ,8,9]]
#  vector
vector = [5,8,1]
#test 1
print(matVec(matrix,vector))
#test 2
print(matVec(vector,matrix))
# test 3
print(matVec("hola",3))
