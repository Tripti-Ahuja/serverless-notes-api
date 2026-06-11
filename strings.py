word = "Python"
print(word[0])
print(word[-1])

print(word[:3])
print(word[3:])
print(word[::-1])


messy = "   ClAuDe Ai   "
messy = messy.strip()
print(messy.lower())

message = "I want a refund please"
if "refund" in message:
    print("Routing to billing")
else:
    print("Routing to support")


sentence1 = "The Cat Sat On The Mat"
words1 = sentence1.split()
print(len(words1))


sentence = "claude is a language model"
words = sentence.split()
#new_sentence = "-".join(words)
print("-".join(words))