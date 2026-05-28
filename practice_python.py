def categorize_digits(num):
    low = 0
    mid = 0
    high = 0
    for digit in str(num):
        digit = int(digit)
        if digit <= 3: #>= 0 and digit <= 3:
            low += 1 
        elif digit <= 6:
            mid += 1
        else:
            high += 1
    return f"low: {low}, mid: {mid}, high : {high}"
        
print(categorize_digits(13579))

    