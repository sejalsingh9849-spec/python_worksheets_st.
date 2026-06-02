def swap_numbers(a, b, choice):

    if choice == 1:
        # Using temporary variable
        temp = a
        a = b
        b = temp

    elif choice == 2:
        # Using arithmetic operators
        a = a + b
        b = a - b
        a = a - b

    elif choice == 3:
        # Using tuple unpacking
        a, b = b, a

    else:
        print("Invalid Choice")
        return

    print("\nAfter Swapping:")
    print("First Number =", a)
    print("Second Number =", b)

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("\nChoose Swapping Method")
print("1. Temporary Variable")
print("2. Arithmetic Method")
print("3. Tuple Unpacking")

choice = int(input("Enter Your Choice: "))

swap_numbers(num1, num2, choice)
