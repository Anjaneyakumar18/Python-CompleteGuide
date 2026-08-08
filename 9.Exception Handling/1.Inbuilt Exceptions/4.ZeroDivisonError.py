numerator = int(input("Enter Numerator: "))
denominator = int(input("Enter Denominator: "))

try:
    if denominator==0:
        raise ZeroDivisionError("Denominator cannot be ZERO")
except Exception as e:
    print(e)
