def findClosestValueInBst(tree, target, closest=None):
    if not tree:
        return closest
    if not closest:
        closest = float('inf')
    if abs(tree.value - target) < abs(target - closest):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBst(tree.right, target, closest)
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
