

k = int(input())
k -= 1

pow_10, length = 1, 1

while 9 * pow_10 * length < k:
    k -= 9 * pow_10 * length
    pow_10 *= 10
    length += 1

div = k / length
rem = k % length

num = pow_10 + div

print(str(num)[rem])
