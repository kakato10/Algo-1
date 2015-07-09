class BST():
    def is_bst(self, array):
        index = len(array) - 1
        is_bst = True
        while index > 0:
            left_child = array[index - 1]
            right_child = array[index]
            parent = array[int((index - 1) / 2)]
            if left_child:
                if left_child > parent:
                    is_bst = False
                    print(left_child, parent, right_child)
                    break
            if right_child:
                if right_child < parent:
                    is_bst = False
                    print(left_child, parent, right_child)
                    break
            index -= 2
        print(is_bst)


def cast(element):
    if element == "None":
        return None
    else:
        return int(element)


def main():
    array = input().split(" ")
    array = list(map(cast, array))
    bst = BST()
    bst.is_bst(array)


if __name__ == '__main__':
    main()
