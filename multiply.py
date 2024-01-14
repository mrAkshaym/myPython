def multiply(a, b):
    return a * b


def main():
    a = int(input("Enter the first number: "))  # Do not change this line
    b = int(input("Enter the second number: ")) # Do not change this line
    result = multiply(a, b)
    print("Multiplying",a,"and", b, "gives:", result) # Do not change this line


    x = float(input("Enter the first float number: "))  # Do not change this line
    y = float(input("Enter the second float number: ")) # Do not change this line
    float_result = multiply(x, y)
    print("Multiplying",x,"and", y, "gives:", float_result) # Do not change this line

if __name__ == "__main__":
    main()