def product_by_n(n):
    total = 1   
    for i in range(1, n +1):
        total *= i     
    return total

print(product_by_n(5))
    