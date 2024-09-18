import math

# Input
n, w, h = map(int, input().split())
diagonal = math.sqrt(w ** 2 + h ** 2)

# Check each match
for _ in range(n):
    match_length = int(input())
    if match_length <= diagonal:
        print("DA")
    else:
        print("NE")
