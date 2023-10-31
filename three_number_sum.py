def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left != right:
            temp = [array[i], array[left], array[right]]
            if sum(temp) > targetSum:
                right -= 1
            elif sum(temp) < targetSum:
                left += 1
            else:
                result.append(temp)
                left += 1
    return result


print(threeNumberSum(array=[12, 3, 1, 2, -6, 5, -8, 6], targetSum=0))


