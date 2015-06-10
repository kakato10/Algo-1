from queue import Queue


class Stack(object):
    def __init__(self):
        self.queue = Queue()

    def push(self, value):
        self.queue.push(value)

    def pop(self):
        new_queue = self.__traverse_queue__()
        value_to_return = self.queue.pop().get_value()
        self.queue = new_queue
        return value_to_return

    def peek(self):
        new_queue = self.__traverse_queue__()
        value_to_return = self.queue.peek()
        new_queue.push(self.queue.pop())
        self.queue = new_queue
        return value_to_return

    def __traverse_queue__(self):
        current_node = None
        new_queue = Queue()
        while not self.queue.get_size() == 1:
            current_node = self.queue.pop()
            new_queue.push(current_node.get_value())
        return new_queue

    def get_size(self):
        return self.queue.get_size()

stack = Stack()
stack.push(4)
print("The first element of the queue is: ", stack.peek())
stack.push(2)
print("The size of the queue is: ", stack.get_size())
print("The popped value from the queue is: ", stack.pop())
print("The queue size after pop is:", stack.get_size())
