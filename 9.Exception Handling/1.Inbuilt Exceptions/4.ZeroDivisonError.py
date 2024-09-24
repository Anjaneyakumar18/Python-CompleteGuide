numerator = int(input("Enter Numerator: "))
denominator = int(input("Enter Denominator: "))

if denominator == 0:
    try:
        raise ZeroDivisionError("Denominator cannot be zero")
    except ZeroDivisionError as e:
        print(e)
else:
    print("Answer is:", numerator / denominator)