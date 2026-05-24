def smallest_odd_digit(num):
    smallest = -1 
    for i in str(num):
        digit = int(i)
        if digit % 2 != 0:
            if smallest == -1 or digit < smallest:
                smallest = digit
    return smallest

print(smallest_odd_digit(57391))
    