def smallest_number(num):
    smallest = 9 
    for i in str(num):
        digit = int(i)
        if digit < smallest: 
            smallest = digit   
    return smallest

print(smallest_number(503))
    