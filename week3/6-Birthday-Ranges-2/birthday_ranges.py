class BirthdayRanges:
    def __init__(self, birthdays_vector):
        self.highest_power_of_two = 0
        while(pow(2, self.highest_power_of_two) < 366):
            self.highest_power_of_two = self.highest_power_of_two + 1
        self.birthdays = [0] * pow(2, self.highest_power_of_two)
        print(pow(2, self.highest_power_of_two))
        for birthday in birthdays_vector:
            self.birthdays[birthday] = self.birthdays[birthday] + 1
        i = len(self.birthdays) - 2
        j = len(self.birthdays) - 1
        while(i >= 0):
            self.birthdays.insert(0, self.birthdays[i] + self.birthdays[j])
            i = i - 1
            j = j - 1

# adds people who are born on a specific day
    def add(self, day, number_of_people):
        sum_of_lower_powers = pow(2, self.highest_power_of_two) - 1
        index = sum_of_lower_powers + day
        while(index > 0):
            self.birthdays[index] = self.birthdays[index] + number_of_people
            index = int((index - 1) / 2)
        self.birthdays[index] = self.birthdays[index] + number_of_people

# removes people who are born on a specific day
    def remove(self, day, number_of_people):
        sum_of_lower_powers = pow(2, self.highest_power_of_two) - 1
        index = sum_of_lower_powers + day
        if (self.birthdays[index] < number_of_people):
            number_of_people = self.birthdays[index]
        while (index > 0):
            self.birthdays[index] = self.birthdays[index] - number_of_people
            index = int((index - 1) / 2)
        self.birthdays[index] = self.birthdays[index] - number_of_people


# returns the number of people born in a range
    def count(self, start_day, end_day):
        return self.query(end_day + 1) - self.query(start_day)

    def query(self, end_day):
        sum_of_lower_powers = pow(2, self.highest_power_of_two) - 1
        current_node_index = sum_of_lower_powers + end_day
        result = 0
        while not current_node_index == 0:
            if current_node_index % 2 == 0:
                result = result + self.birthdays[current_node_index - 1]
            current_node_index = int((current_node_index - 1) / 2)
        return result
