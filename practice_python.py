def sum_between(a, b):
    total = 0   
    for i in range(a, b+1):
        total += i     
    return total

print(sum_between(3, 7))
    