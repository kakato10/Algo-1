class Vector(object):

    def __init__(self, capacity):
        self.list = [None] * capacity
        self.size = 0

    def insert(self, index, value):
        if not index == 0 and index > self.size:
            return False
        else:
            self.__should_grow__()
            self.list[index] = value

    def add(self, value):
        self.__should_grow__()
        self.list[self.size] = value
        self.size = self.size + 1

    def remove(self, index):
        removed_element = None
        i = 0
        while i < self.size:
            if i >= self.size:
                break
            if i == index:
                removed_element = self.list[i]
                while i < self.size - 1:
                    self.list[i] = self.list[i + 1]
                    i = i + 1
                self.list[i] = None
            i = i + 1
        self.size = self.size - 1
        self.__should_shrink__()
        return removed_element

    def pop(self):
        removed_element = self.list[self.size - 1]
        self.list[self.size - 1] = None
        self.size = self.size - 1
        self.__should_shrink__()
        return removed_element

    def get(self, index):
        return self.list[index]

    def get_size(self):
        return self.size

    def get_capacity(self):
        return len(self.list)

    def print_vector(self):
        i = 0
        while i < self.size:
            print(self.list[i])
            i = i + 1

    def __should_grow__(self):
        if self.size == len(self.list):
            new_list = [None] * 2 * len(self.list)
            for index, element in enumerate(self.list):
                new_list[index] = self.list[index]
            self.list = new_list

    def __should_shrink__(self):
        if self.size <= len(self.list) / 4:
            new_list = [None] * int(len(self.list) / 2)
            index = 0
            while index < len(new_list):
                new_list[index] = self.list[index]
                index = index + 1
            self.list = new_list
