class Roots:

    def square_root(self, number):
        if number < 1:
            print(format(self.binary_search(0, 1, number), '.5f'))
        else:
            print(format(self.binary_search(0, number, number), '.5f'))

    def binary_search(self, start, end, number):
        middle = (end + start) / 2
        square = middle * middle
        if (abs(number - middle * middle) < 0.00001):
            return middle
        elif (square > number):
            if (number > 1):
                end = middle
            else:
                start = middle
        else:
            if (number > 1):
                start = middle
            else:
                end = middle
        return float(self.binary_search(start, end, number))


def main():
    number = int(input())
    t = Roots()
    t.square_root(number)

if __name__ == '__main__':
    main()
