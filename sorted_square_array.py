def sortedSquaredArray(array):
    if len(array) == 1:
        return [array[0] * array[0]]
    result = []
    left_pointer = 0
    right_pointer = -1
    while len(result) != len(array):
        if abs(array[left_pointer]) >= abs(array[right_pointer]):
            result.insert(0, abs(array[left_pointer]) * abs(array[left_pointer]))
            left_pointer += 1
        if abs(array[right_pointer]) > abs(array[left_pointer]):
            result.insert(0, abs(array[right_pointer]) * abs(array[right_pointer]))
            right_pointer -= 1
    return result


print(sortedSquaredArray([-4, -2, 1, 3]))
