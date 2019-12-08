"""
Given a range of 6 digit numbers, find all numbers in the range
which match these criteria:
    * All digits in the number are in non-decreasing order.
    Part 1:
        * At least two of the digits in the number need to be same.
    Part 2:
        * Two of the digits in the number need to be same and not port of a
          larger group of digits.
"""

def get_digits_list(number):
    """
    Reads a number and returns a list of digits in the number
    """
    output = []
    divider = 10

    while number > 0:
        output.append(number % divider)
        number = int(number/divider)

    output.reverse()
    return output


def check_password_criteria(digits_list, part):
    """
    Checks if the given input list of numbers matches the password criteria:
        * All digits in the number are in non-decreasing order.
        * Two of the digits in the number need to be same.
    :param digits_list: A list of numbers in [0-9]
    :param part: 1 or 2
    :return: True or False
    """
    # Verify that the list is sorted.
    if sorted(digits_list) != digits_list:
        return False

    if part == 1:
        # Verify that exactly one number in the list is repeated.
        return len(set(digits_list)) <= len(digits_list) - 1
    elif part == 2:
        counts = {}
        for digit in digits_list:
            counts[digit] = counts.get(digit, 0) + 1
        if 2 in counts.values():
            return True
        else:
            return False

    return False

def get_number(digits_list):
    """
    Converts a given list of digits into an integer
    """
    multiplier = 1
    output = 0
    reversed_digits = reversed(digits_list)
    for n in reversed_digits:
        output += n * multiplier
        multiplier *= 10

    # Realized after writing this that it could be a one liner
    # return int("".join([str(k) for k in digits_list]))
    return output


def get_numbers(range_min, range_max):
    """
    Returns all numbers in the specified range which meet the password criteria.
    :param range_min: Specifies the starting number.
    :param range_max: Specifies the ending number.
    :return: List of numbers
    """
    output = []
    for num in range(range_min, range_max + 1):
        digits_list = get_digits_list(num)
        if check_password_criteria(digits_list, 2):
            output.append(get_number(digits_list))

    # print(output)
    return output


def main():
    range_min = 125730
    range_max = 579381

    possible_passwords = get_numbers(range_min, range_max)
    print(len(possible_passwords))


if __name__ == '__main__':
    main()
