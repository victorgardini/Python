# Problem: Given an int, repeatedly add its digits until the result is one digit.

# wiki: - https://en.wikipedia.org/wiki/Digital_root

def add_digits(num: int) -> int:
    if num < 10:
        return num
    return add_digits(sum(int(digit) for digit in str(num)))
