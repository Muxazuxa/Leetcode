def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] == toMove:
            if array[right] != toMove:
                array[right], array[left] = array[left], array[right]
                left += 1
            right -= 1
        elif array[left] != toMove and array[right] != toMove:
            left += 1
        else:
            left += 1
            right -= 1
    return array
