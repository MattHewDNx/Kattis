# Read the grading limits
a, b, c, d, e = map(int, input().split())

# Read the exam score
score = int(input())

# Determine the grade based on the score and grading limits
if score >= a:
    print("A")
elif score >= b:
    print("B")
elif score >= c:
    print("C")
elif score >= d:
    print("D")
elif score >= e:
    print("E")
else:
    print("F")
