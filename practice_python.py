def second_largest_number(num):
    largest = -1
    second_largest = -1
    for digit in str(num):
        digit = int(digit)
        if digit > largest:
            second_largest = largest
            largest = digit
        elif digit < largest and digit > second_largest:
            second_largest = digit
    return second_largest


print(second_largest_number(19345))
    

    