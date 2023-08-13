# Read input numbers
a, b = input().split()

# Reverse the numbers and compare them
a_reversed = int(a[::-1])
b_reversed = int(b[::-1])

# Find the larger of the two reversed numbers
larger_reversed = max(a_reversed, b_reversed)



# Print the result
print(larger_reversed)
