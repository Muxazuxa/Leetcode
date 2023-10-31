def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    first_pointer = 0
    second_pointer = 0
    min_value = float('inf')
    while first_pointer < len(arrayOne) and second_pointer < len(arrayTwo):
        if abs(arrayOne[first_pointer] - arrayTwo[second_pointer]) < min_value:
            min_value = abs(arrayOne[first_pointer] - arrayTwo[second_pointer])
            ans = [arrayOne[first_pointer], arrayTwo[second_pointer]]
        if arrayOne[first_pointer] > arrayTwo[second_pointer]:
            second_pointer += 1
        else:
            first_pointer += 1

    return ans


print(smallestDifference(arrayOne=[-1, 5, 10, 20, 28, 3], arrayTwo=[26, 134, 135, 15, 17]))

