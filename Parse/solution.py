from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    
    values = list_repr.split(" -> ")[:-1]
    
    head = None
    for val in reversed(values):
        head = Node(int(val), head)
    
    return head