class RangeMinimumQuery():
    def __init__(self, array):
        self.array = array

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def heapify(self, array):
        self.heap = []
        for el in array:
            self.heap.append(el)
            index = len(self.heap) - 1
            parent_index = int((index - 1) / 2)
            while not index == 0 and el < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = int((index - 1) / 2)

    def set(self, index, value):
        self.array[index] = value

    def get_min(self, start, end):
        array = self.array[start: end + 1]
        self.heapify(array)
        print(self.heap[0])


def main():
    initial_input = input().split(" ")
    commands_count = int(initial_input[1])
    array = input().split(" ")
    array = list(map(int, array))
    ranger = RangeMinimumQuery(array)
    while commands_count > 0:
        command = input().split(" ")
        if command[0] == "min":
            ranger.get_min(int(command[1]), int(command[2]))
        elif command[0] == "set":
            ranger.set(int(command[1]), int(command[2]))
        commands_count -= 1

if __name__ == '__main__':
    main()
