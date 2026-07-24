def get_number(num):
    while True:
        Op = input("Number "+ str(num)+": ")
        try:
            return float(Op)
        except:
            print("Invalid input. Try Again.")

op1 = get_number(1)
op2 = get_number(2)
sign = input("Operator :")

result = 0
if sign == "+":
    result = op1 + op2
elif sign == "-":
    result = op1 - op2
elif sign == "*":
    result = op1 * op2
elif sign == "/":
    if op2 == 0:
        print("Error: Division by zero.")
    else:
        result = op1 / op2
else:
    print("Invalid operator. Please use +, -, *, or /.")

print("Result:", result)