def classify_number(n):
    if n == 0:
        return "Zero"
    elif n < 0:
        return "negative"
    elif n > 0 and n % 2 == 0:
        return "positive even"
    elif n > 0 and n % 2 != 0:
        return "positive odd"
    
print(classify_number(2))
    

    