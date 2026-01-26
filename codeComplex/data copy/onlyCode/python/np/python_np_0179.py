import itertools

n, l, r, x = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

counter = 0
for i, val in enumerate(["".join(seq) for seq in itertools.product("01", repeat=n)]):
    if val.count('1') < 2:
        continue
    dif = 0; mx = float("-inf"); mn = float("inf")
    for i, bit in enumerate(val):
        if bit == '1':
            dif += c[i]
            mx = max(c[i], mx)
            mn = min(c[i], mn)
    if l <= dif <= r and  mx - mn >= x:
        counter += 1

print(counter)
