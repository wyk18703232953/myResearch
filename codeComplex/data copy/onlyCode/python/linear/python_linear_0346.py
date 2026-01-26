a, b = map(int, input().split())
q, r = divmod(a, 2)
print('01'*q + '0'*r)
