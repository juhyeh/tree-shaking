def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"


def square(x):
    return x**2


def cube(x):
    return x**3


# Example usage
def main():
    print("Starting program...")

    num1 = 3
    num2 = 45

    num3 = add(num1, num2)  # 48
    num4 = subtract(num3, num1)  # 45
    num5 = divide(num4, num1)  # 15
    num6 = multiply(num5, num1)  # 45

    print(
        f"num2: {num2}, \nnum4: {num4},\nand num6: {num6} \nare all 45: \n{num1 == num4 == num6}"
    )

    print("Ending program...")


if __name__ == "__main__":
    main()
