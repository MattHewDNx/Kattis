# Input
pieces = list(map(int, input().split()))

# Expected counts of each piece
expected_counts = [1, 1, 2, 2, 2, 8]

# Calculate the differences between the found pieces and the expected counts
differences = [expected - found for expected, found in zip(expected_counts, pieces)]

# Output the differences
print(*differences)
