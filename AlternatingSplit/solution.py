class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second): 
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List too short")

    first = head
    second = head.next

    first_current = first
    second_current = second

    while first_current and second_current:
        first_current.next = second_current.next
        first_current = first_current.next

        if first_current:
            second_current.next = first_current.next
            second_current = second_current.next
        else:
            second_current.next = None

    return Context(first, second)