from random import choice


class RandSet():
    def __init__(self):
        self.mod = 2
        self.resizing_factor = 0.7
        self.collection = list()
        self.populate_empty_collection(self.collection, self.mod)
        self.indexes = set()

    def insert(self, number):
        print("Want to insert, ", number)
        if len(self.indexes) / len(self.collection) < self.resizing_factor:
            hashed = self.hash(number)
            self.indexes.add(hashed)
            if number not in self.collection[hashed]:
                self.collection[hashed].append(number)
            else:
                return
        else:
            self.resize_collection()
            self.insert(number)
        print(self.collection)

    def remove(self, number):
        hashed = self.hash(number)
        self.collection[hashed].remove(number)
        if len(self.collection[hashed]) == 0:
            self.indexes.remove(hashed)

    def random(self):
        print(choice(self.collection[choice(list(self.indexes))]))

    def contains(self, number):
        hashed = self.hash(number)
        if number not in self.indexes:
            print(False)
        else:
            print(number in self.collection[hashed])

    def resize_collection(self):
        self.mod *= 2
        array = list()
        self.populate_empty_collection(array, self.mod)
        current_collection = self.collection
        self.collection = list()
        self.populate_empty_collection(self.collection, self.mod)
        current_indexes = self.indexes
        self.indexes = set()
        for index in current_indexes:
            for element in current_collection[index]:
                self.insert(element)

    def hash(self, number):
        return number % self.mod

    def populate_empty_collection(self, collection, counter):
        while counter > 0:
            collection.append([])
            counter -= 1
# check with insert 2, insert 3, insert 5


def main():
    commands_count = int(input("Enter count of commands:"))
    rand_set = RandSet()
    while commands_count > 0:
        command = input("command> ").split(" ")
        if command[0] == "insert":
            rand_set.insert(int(command[1]))
        elif command[0] == "remove":
            rand_set.remove(int(command[1]))
        elif command[0] == "contains":
            rand_set.contains(int(command[1]))
        elif command[0] == "random":
            rand_set.random()
        commands_count -= 1

if __name__ == '__main__':
    main()
