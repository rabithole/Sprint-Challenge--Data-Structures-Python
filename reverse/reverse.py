class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node
        # print('Add to head:', value)

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    def reverse_list(self, node, prev):        
        if node is None:
            # print(node)
            return None
        # if list has only 1 node
        if node.next_node is None:
            self.head = node
            # print('Node = head', node.value)
            return node

        temporary_node = self.reverse_list(node.get_next(), node)
        # print('temporary_node', temporary_node.value)
        temporary_node.next_node = node
        # print('next temp', node.value)
        node.set_next(None)
        # print(node.value)

        return node

rev = LinkedList()
