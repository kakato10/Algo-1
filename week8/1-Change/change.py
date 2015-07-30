class Change():
    def __init__(self):
        self.coins = [1, 2, 5, 10, 20, 50, 100]
        self.results = {}

    def calculate(self, number, max_coin_id):
        i = max_coin_id
        ways = 0
        if max_coin_id < 0:
            return 0
        if max_coin_id == 0 or number == 1 or number == 0:
            return 1
        if (number, max_coin_id) in self.results:
            return self.results[(number, max_coin_id)]
        while i >= 0:
            if (self.coins[i] > number):
                i -= 1
            else:
                ways += self.calculate(number, i - 1)
                ways += self.calculate(number - self.coins[i], i)
                i -= 1
                break
        self.results[(number, max_coin_id)] = ways
        return ways


def main():
    number = int(input("Enter a number:"))
    change = Change()
    print(change.calculate(number, 6))

if __name__ == '__main__':
    main()
