def isValidSubsequence(array, sequence):
    for i in array:
        if sequence and i == sequence[0]:
            del sequence[0]
    return not bool(sequence)
