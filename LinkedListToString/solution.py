def stringify(node):
    if node is None:
        return "None"
    return str(node.data) + " -> " + stringify(node.next)