class Heap():
    def __init__(self, array):
        self.array = array
        self.heapify()

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def heapify(self):
        self.heap = []
        for el in self.array:
            self.heap.append(el)
            index = len(self.heap) - 1
            parent_index = int((index - 1) / 2)
            while not index == 0 and el < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = int((index - 1) / 2)

    def remove(self):
        self.swap(0, len(self.heap) - 1)
        root = self.heap[-1]
        del self.heap[-1]
        item_index = 0
        left_child = item_index * 2 + 1
        right_child = item_index * 2 + 2
        while left_child < len(self.heap):
            if right_child < len(self.heap):
                if self.heap[left_child] < self.heap[right_child]:
                    compare_to = left_child
                else:
                    compare_to = right_child
            else:
                compare_to = left_child
            if self.heap[item_index] > self.heap[compare_to]:
                self.swap(item_index, compare_to)
            else:
                break
            item_index = compare_to
            left_child = item_index * 2 + 1
            right_child = item_index * 2 + 2
        return root

    def get_k_min(self, k):
        self.array = []
        while len(self.array) < k:
            self.array.append(self.remove())
        print(self.array[-1])


def main():
    initial_input = input().split(" ")
    k = int(initial_input[1])
    array = input().split(" ")
    array = list(map(int, array))
    heap = Heap(array)
    heap.get_k_min(k)


if __name__ == '__main__':
    main()
