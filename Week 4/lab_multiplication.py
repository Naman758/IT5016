def multiplication_table(number, up_to=10):
    """Generate and display a multiplication table using a for loop."""
    print(f"Multiplication table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

#Generate a multiplication table for the number 7
multiplication_table(int(input("Enter a number:"))) 