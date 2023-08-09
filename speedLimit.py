def calculate_distance(log):
    total_distance = 0
    prev_time = 0
    for speed, time in log:
        total_distance += speed * (time - prev_time)
        prev_time = time
    return total_distance

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        log = []
        for _ in range(n):
            speed, time = map(int, input().split())
            log.append((speed, time))
        distance = calculate_distance(log)
        print(distance, "miles")

if __name__ == "__main__":
    main()
