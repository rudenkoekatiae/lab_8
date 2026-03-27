from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
class ArgumentException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def get_nth(node, index):
    current = node
    i = 0
    while current is not None:
        if i == index:
            return current
        current = current.next
        i += 1
    raise Exception("Index out of bounds")