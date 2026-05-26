def largest_digit(num):
    largest = 0
    for digit in str(num):
        digit = int(digit)
        if digit > largest:
            largest = digit
    return largest

print(largest_digit(7))
    