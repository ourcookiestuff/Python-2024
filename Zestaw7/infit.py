import random


class InfiniteBinaryIterator:
    """Klasa iteratora binarnego zwracająca 0, 1, 0, 1, ..."""
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.counter
        self.counter = (self.counter + 1) % 2
        return result


class RandomDirectionIterator:
    """Klasa iteratora zwracająca losowy kierunek ("N", "E", "S", "W")"""
    def __init__(self):
        self.directions = ("N", "E", "S", "W")

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)


class WeeklyDayIterator:
    """Klasa iteratora zwrcająca: 0, 1, 2, 3, 4, 5, 6, 0, 1, ..."""
    def __init__(self):
        self.counter = 0
        self.values = (0, 1, 2, 3, 4, 5, 6)

    def __iter__(self):
        return self

    def __next__(self):
        result = self.values[self.counter]
        self.counter = (self.counter + 1) % 7
        return result

