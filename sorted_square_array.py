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
        else:
            result.insert(0, abs(array[right_pointer]) * abs(array[right_pointer]))
            right_pointer -= 1
    return result
