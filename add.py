def add_numbers(a, b):
    return a + b

def main():
    # Your code here
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = add_numbers(num1, num2)
    print("Adding", num1, "and", num2, "gives:", result)

if __name__ == "__main__":
    main()
