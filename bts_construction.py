# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, value):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#         action = True
#         while action:
#             if value > self.value:
#
#         return self
#
#     def contains(self, value):
#         # Write your code here.
#         if value > self.value:
#             if not self.right:
#                 return False
#             return self.right.contains(value)
#         elif value < self.value:
#             if not self.left:
#                 return False
#             return self.left.contains(value)
#         return True
#
#     def remove(self, value):
#         if value > self.value:
#             if not self.right:
#                 self.right = self.__class__(value)
#                 return self
#             return self.right.insert(value)
#         elif value < self.value:
#             if not self.left:
#                 self.left = self.__class__(value)
#                 return self
#             return self.left.insert(value)
#         return self
