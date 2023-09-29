# Function to find the odd man out
def find_odd_man_out(test_case, guests):
    guest_count = {}
    
    for guest in guests:
        if guest in guest_count:
            guest_count[guest] += 1
        else:
            guest_count[guest] = 1
    
    for guest, count in guest_count.items():
        if count == 1:
            return f"Case #{test_case}: {guest}"

# Read the number of test cases
num_cases = int(input())

# Process each test case
for test_case in range(1, num_cases + 1):
    num_guests = int(input())
    guest_list = list(map(int, input().split()))
    
    result = find_odd_man_out(test_case, guest_list)
    print(result)
