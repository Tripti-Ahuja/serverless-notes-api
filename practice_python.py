def count_digits(num):
    total = 0   
    for i in str(num):
        total += int(i)     
    return total

print(count_digits(1234))
    