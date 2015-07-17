class BST():
    def is_bst(self, array):
        is_bst = self.check_bst(array, 0, None, None)
        if(is_bst):
            print("YES")
        else:
            print("NO")

    def check_bst(self, array, subroot_index, min_value, max_value):
        if len(array) == 0:
            return True
        if subroot_index >= len(array):
            return True
        value = array[subroot_index]
        if value == 0:
            return True
        if min_value:
            if value < min_value:
                return False
        if max_value:
            if value > max_value:
                return False
        left_child = subroot_index * 2 + 1
        right_child = left_child + 1
        left_subtree = self.check_bst(array, left_child, min_value, value)
        right_subtree = self.check_bst(array, right_child, value, max_value)
        return left_subtree and right_subtree


def cast(element):
    if element == "None":
        return None
    else:
        return int(element)


def main():
    size = input()
    array = input().split(" ")
    array = list(map(cast, array))
    bst = BST()
    bst.is_bst(array)


if __name__ == '__main__':
    main()
