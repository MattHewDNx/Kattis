a = input()

b = a.count('b')
k = a.count('k')

if b == 0 and k == 0 :
    print('none')
elif b > k:
    print('boba')
elif k > b :
    print('kiki')
else:
    print('boki')
