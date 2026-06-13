"""score = 8
if score >= 6:
    print("Pass")
else:
    print("Fail")"""

"""marks = 62
if marks >= 90:
    print("A")
elif marks >= 75 and marks <= 89:
    print("B")
elif marks >= 60 and marks <= 74:
    print("C")
else:
    print("F")"""

"""temperature = 0.5
has_key = False
if temperature <= 0.7 and has_key == True:
    print("Running")
else:
    print("Cannot run")"""


"""user_input = ""
if user_input:
    print("Got it")
else:
    print("Please type something")"""

"""message = ""
if message:
    if "refund" in message:
        print("Routing to billing")
    elif "password" in message:
        print("Routing to security")
    elif "slow" in message:
        print("Routing to tech support")
    else:
        print("Routing to general support")
else:
    print("No message received")"""


"""username = "tripti"
password = "claude456"
if username == "Tripti" and password == "claude123":
    print("Login successful")
elif username == "Tripti" and password != "claude123":
    print("Wrong password")
elif username != "Tripti":
    print("User not found")"""


"""temperature = 0.95
if temperature == 0.0:
    print("Fully deterministic")
elif temperature <= 0.3:
    print("Precise")
elif temperature <= 0.7:
    print("Balanced")
else:
    print("Creative")"""


message = ""    #input("Enter your support message: ")
clean = message.strip().lower()
if not clean:
    print("No message received")
else:
    preview = clean[:20]
    Words = len(clean.split())
    if "refund" in clean or "payment" in clean:
        department = "Billing"
    elif "password" in clean or "login" in clean:
        department = "Security"
    elif "slow" in clean or "down" in clean or "error" in clean:
        department = "Tech Support"
    else:
        department = "General"


    if "down" in clean or "urgent" in clean or "broken" in clean:
        priority = 3
    elif "slow" in clean or "error" in clean:
        priority = 2
    else:
        priority = 1

    print("--- Ticket Report ---")
    print(f"Preview: {preview}")
    print(f"Words: {Words}")
    print(f"Department: {department}")
    print(f"Priority: {priority}")


