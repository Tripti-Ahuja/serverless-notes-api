def largest_number(num):
    largest = -1 
    for i in str(num):
        digit = int(i)
        if digit > largest: 
            largest = digit   
    return largest

print(largest_number(1934))
    