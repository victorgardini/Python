# Problem: Create a class with an insert method to insert an int to a list.
# It should also support calculating the max, min, mean, and mode in O(1).


class Solution:
    def __init__(self, upper_limit=100):
        self.max = None
        self.min = None

        self.mean = None
        self.count_items = 0
        self.sum = 0

        self.array = [0] * (upper_limit + 1)
        self.mode_occurrences = 0
        self.mode = None

    def insert(self, num):
        if not isinstance(num, int):
            raise TypeError('num must be an int')

        # set max and min if they are not set or if num is greater or less than
        if self.max is None or num > self.max:
            self.max = num
        if self.min is None or num < self.min:
            self.min = num

        # update mean
        self.count_items += 1
        self.sum += num
        self.mean = self.sum / self.count_items

        self.array[num] += 1  # increment the count of the number
        if self.array[num] > self.mode_occurrences:  # update mode
            self.mode = num  # set the mode to the number
            self.mode_occurrences = self.array[num]  # set the mode occurrences to the count of the number
