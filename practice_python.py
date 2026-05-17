def sum_of_digits(num):
    total = 0   
    for char in str(num):
        total += int(char)     
    return total

print(sum_of_digits(1234))
    