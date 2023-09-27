a = int(input())

for _ in range(a):
    b = int(input())
    fact = 1

    # Calculate the factorial of 'b'
    for j in range(1, b + 1):
        fact *= j

    # Extract and print the last digit of the factorial
    last_digit = fact % 10
    print(last_digit)
