def transposeMatrix(matrix):
    # Write your code here.
    result = []
    for i in range(len(matrix[0])):
        result.append([])
        for j in range(len(matrix)):
            result[-1].append(matrix[j][i])
    return result
