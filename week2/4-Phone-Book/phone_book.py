class PhoneBook():
    def __init__(self, phone_book):
        self.phone_book = phone_book
        self.sort_phone_book()

    def find(self, number, start, end):
        middle = int((end + start) / 2)
        current_number = self.phone_book[middle][0]
        if current_number == number:
            return self.phone_book[middle][1]
        elif (current_number > number):
            end = middle
        else:
            start = middle
        return self.find(number, start, end)

    def find_numbers(self, numbers):
        for number in numbers:
            print(self.find(number, 0, len(self.phone_book)))

    def sort_phone_book(self):
        self.phone_book = sorted(self.phone_book, key=lambda tup: tup[0])


def main():
    lengths = input().split(" ")
    book_length = int(lengths[0])
    searched_numbers_length = int(lengths[1])
    phone_book = []
    counter = 0
    while counter < book_length:
        phone_book.append(input().split(" "))
        phone_book[counter][0] = int(phone_book[counter][0])
        counter = counter + 1
    counter = 0
    searched_numbers = []
    while counter < searched_numbers_length:
        searched_numbers.append(int(input()))
        counter = counter + 1
    phone_book = PhoneBook(phone_book)
    phone_book.find_numbers(searched_numbers)

if __name__ == '__main__':
    main()
