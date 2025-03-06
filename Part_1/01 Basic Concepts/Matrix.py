# Matrix example
a = ((2, 3, 4), (5, 6, 7), (8, 9, 10))
b = (4, 7, 10)

print(a)
print(b)
print(" ")

def elementwise_multiplication(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Количество столбцов в матрице должно совпадать с длиной вектора")

    result = []
    for row in matrix:
        result.append(tuple(row[i] * vector[i] for i in range(len(vector))))

    return tuple(result)




def dot_product(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Number of columns in the matrix must match the length of the vector")

    return tuple(sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix)



result = elementwise_multiplication(a, b)
print("Element-wise matrix multiplication\n", result)  # Result: ((8, 21, 40), (20, 42, 70), (32, 63, 100))


result = dot_product(a, b)
print("\nMatrix-vector dot product\n",result)  # Result: (69, 132, 195)
