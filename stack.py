class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def push(self, value):
        if self.has_space():
            item_to_add = Node(value)
            item_to_add.set_next_node(self.top_item)
            self.top_item = item_to_add
            self.size += 1
        else:
            print("The stack is full")

    def pop(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 0
            return item_to_remove.get_value()

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            return self.top_item.get_value()

#book_stack = Stack(0)
#book_stack.pop()

record_stack = Stack(5)
record_stack.push("Ummagumma")
record_stack.push("Bloom")
record_stack.push("Veckatimest")
record_stack.push("It Still Moves")
record_stack.push("High Violet")

print("The current record is " + record_stack.peek())

record_stack.pop()
record_stack.pop()

print("The current record is " + record_stack.peek())