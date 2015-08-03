class MaxBanana():
    def __init__(self):
        self.get_map()

    def get_map(self):
        self.path = []
        self.size = int(input())
        counter = 0
        while counter < self.size:
            new_row = input().split(" ")
            self.path.append(list(map(int, new_row)))
            counter += 1
        print(self.max_bananas(self.size - 1, 0))

    def max_bananas(self, x, y):
        if x == 0 or y == self.size - 1:
            if y + 1 > self.size - 1:
                return self.path[x][y]
            else:
                return self.path[x][y] + self.max_bananas(x, y + 1)
        elif y == self.size - 1:
            if x - 1 < 0:
                return self.path[x][y]
            else:
                return self.path[x][y] + self.max_bananas(x - 1, y)
        print(x, y)
        best_subtree = max(self.max_bananas(x - 1, y), self.max_bananas(x, y + 1))
        return self.path[x][y] + best_subtree


def main():
    bananas = MaxBanana()

if __name__ == '__main__':
    main()
