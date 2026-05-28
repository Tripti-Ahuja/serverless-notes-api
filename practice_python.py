def smallest_digit_above_5(num):
    smallest = 10
    for digit in str(num):
        digit = int(digit)
        if digit > 5 and digit < smallest:
            smallest = digit
    if smallest == 10:
            return -1
    return smallest

print(smallest_digit_above_5(67890))
    

    