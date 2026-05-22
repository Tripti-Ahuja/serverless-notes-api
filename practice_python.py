def largest_even_digit(num):
    largest = -1 
    for i in str(num):
        digit = int(i)
        if digit % 2 == 0:
            if digit > largest:
                largest = digit
    return largest

print(largest_even_digit(1934))
    