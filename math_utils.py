def sum_of_squares(lists_of_digits):
    x = 0
    for digit in lists_of_digits:
        x += digit**2
    return x