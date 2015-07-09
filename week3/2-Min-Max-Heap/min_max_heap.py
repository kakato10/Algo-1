class MinMaxHeap():
    def is_min_max_heap(self, array):
        result = True
        i = 0
        level = 1
        next_level = self.get_next_level_index(i)
        while i < len(array):
            if i == next_level:
                next_level = self.get_next_level_index(i)
                level += 1
            left_child_index = i * 2 + 1
            left_child = None
            right_child_index = left_child_index + 1
            right_child = None
            # get left child if exists
            if (left_child_index < len(array)):
                left_child = array[left_child_index]
                # get right child if exists
                if (right_child_index < len(array)):
                    right_child = array[right_child_index]
            if level % 2 == 1:
                # odd level rulse
                if left_child:
                    if array[i] > left_child:
                        result = False
                        break
                    if right_child:
                        if array[i] > right_child:
                            result = False
                            break
            else:
                # even level rules
                if left_child:
                    if array[i] < left_child:
                        result = False
                        break
                    if right_child:
                        if array[i] < right_child:
                            result = False
                            break
            i += 1
        print(result)

    def get_next_level_index(self, i):
        return i * 2 + 1


def main():
    array = input().split(" ")
    array = list(map(int, array))
    checker = MinMaxHeap()
    checker.is_min_max_heap(array)

if __name__ == '__main__':
    main()
