while True:
    op = input("choose an operation (+, -, *, /, ^): ")
    if op in "+-*/^":
        break
    else:
        print("No, pick an actual operation")

def calculator(a, b, op):
    # op means operator
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "can't divide by zero boo"
        else:
            return a/b
    elif op == "^":
        return a ** b

    else:
        return "invalid operation"

while True:
    try:
        a = float(input("First: "))
        b = float(input("Second: "))
        break
    except ValueError:
        print("aloo, enter numbers only")

result = calculator(a, b, op)

print(f"Result: {result}")