def greeting(name):
    print("Hello", name)

def add(a, b):
    sum = a+b
    print("The sum of ", a, "and ", b, " is ", sum)

def add_inputs():
    a = float(input("Enter the first number "))
    b = float(input("Enter the second number "))
    sum = a+b
    print("The sum of",a,"and",b,"is",sum) #The sum of 4.0 and 3.0 is 7.0

    if (a.is_integer()):
        a_str = str(int(a))
    else:
        a_str = str(a)

    if (b.is_integer()):
        b_str = str(int(b))
    else:
        b_str = str(b)

    if (sum.is_integer()):
        sum_str = str(int(sum))
    else:
        sum_str = str(sum)

    print("The sum of "+a_str +" and "+ b_str+ " is "+ sum_str)
    

if __name__ == "__main__":
    #
    '''
    add(2,5)
    add(3.4, 2.1)
    
    greeting("Shubham")
    greeting("Rahul")
    greeting("Vikram")
    '''
    more = True;
    while (more):
        add_inputs()
        more = (input("more sum ? y/n") == "y")
    