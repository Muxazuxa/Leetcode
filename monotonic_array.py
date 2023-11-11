def isMonotonic(array):
    # Write your code here.
    if not array or len(array) == 1:
        return True
    if not array[0] == array[1]:
        increasing = True if array[0] < array[1] else False
    else:
        increasing = True if array[1] < array[2] else False
    for i in range(len(array) - 1):
        if increasing:
            if array[i] > array[i + 1]:
                return False
        else:
            if array[i] < array[i + 1]:
                return False
    return True
