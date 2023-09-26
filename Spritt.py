a, b = map(int, input().split())
sum = 0

for i in range(a):
    c = int(input())
    sum += c

if sum > b:
    print('Neibb\n')
if sum ==b:
    print('Jebb\n')
if sum <b:
    print('Jebb\n')