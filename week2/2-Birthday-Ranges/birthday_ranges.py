class BirthdayRanges:
    def __init__(self, birthdays):
        self.birthdays = [0] * 366
        for birthday in birthdays:
            self.birthdays[birthday] = self.birthdays[birthday] + 1
        for i, birthday in enumerate(self.birthdays):
            if not i == 0:
                self.birthdays[i] = self.birthdays[i] + self.birthdays[i - 1]

    # Return a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]
    def birthdays_count(self, the_range):
        start = int(the_range[0])
        end = int(the_range[1])
        if start == 0:
            print(self.birthdays[end])
        else:
            print(self.birthdays[end] - self.birthdays[start - 1])


def main():
    user_input = input()
    ranges_count = int(user_input.split(" ")[1])
    birthdays = input().split(" ")
    birthdays = list(map((lambda x: int(x)), birthdays))
    counter = 1
    unit = BirthdayRanges(birthdays)
    while counter <= ranges_count:
        the_range = input().split(" ")
        unit.birthdays_count(the_range)
        counter = counter + 1

if __name__ == '__main__':
    main()
