# Function to count the number of distinct cities Alice has visited for a single test case
def count_distinct_cities(trips):
    visited_cities = set()  # Use a set to store unique city names
    for city in trips:
        visited_cities.add(city)
    return len(visited_cities)

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    num_trips = int(input())
    trips = []
    
    # Read the city names for this test case
    for _ in range(num_trips):
        city = input().strip()
        trips.append(city)
    
    # Count the number of distinct cities for this test case and print the result
    distinct_cities = count_distinct_cities(trips)
    print(distinct_cities)
