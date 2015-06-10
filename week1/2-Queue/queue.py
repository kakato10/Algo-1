from node import Node


class Queue():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, value):
        if self.size == 0:
            self.size = self.size + 1
            self.head = Node(value)
        else:
            node = Node(value)
            if not self.tail:
                self.tail = node
                self.tail.change_previous_node(self.head)
                self.head.change_next_node(self.tail)
            else:
                self.tail.change_next_node(node)
                node.change_previous_node(self.node)
                self.tail = node
            self.size = self.size + 1

    def pop(self):
        element_to_pop = self.head
        self.head = self.head.get_next_node()
        self.size = self.size - 1
        return element_to_pop

    def get_size(self):
        return self.size

    def peek(self):
        return self.head.get_value()

queue = Queue()
queue.push(4)
print("The first element of the queue is: ", queue.peek())
queue.push(2)
print("The size of the queue is: ", queue.get_size())
print("The popped value from the queue is: ", queue.pop().get_value())
print("The queue size after pop is:", queue.get_size())
