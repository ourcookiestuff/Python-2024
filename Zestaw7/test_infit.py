from infit import *


def test_iterators():
    # Test InfiniteBinaryIterator
    print("Testing InfiniteBinaryIterator:")
    binary_iterator = InfiniteBinaryIterator()
    print([next(binary_iterator) for _ in range(10)])

    # Test RandomDirectionIterator
    print("Testing RandomDirectionIterator:")
    direction_iterator = RandomDirectionIterator()
    print([next(direction_iterator) for _ in range(10)])

    # Test WeeklyDayIterator
    print("Testing WeeklyDayIterator:")
    weekly_iterator = WeeklyDayIterator()
    print([next(weekly_iterator) for _ in range(14)])


if __name__ == "__main__":
    test_iterators()
