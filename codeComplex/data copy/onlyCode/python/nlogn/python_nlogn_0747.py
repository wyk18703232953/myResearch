n = int(input())

a = list(map(lambda i: int(i), input().split(sep=' ')))
a.sort()
a_count = len(a)

b = list(filter(lambda i: i > 0, a))
b_count = len(b)

def resh():
    idx = 1
    while idx < a_count:
        if a[idx] == a[idx - 1] and (a[idx] - 1) in a:
            return 'cslnb'
        idx += 1

    b_sum = sum(b)
    v_sum = sum(range(1, b_count if a_count == b_count else b_count + 1))
    t = max(b_sum - v_sum, 0)
    return 'cslnb' if t % 2 == 0 else 'sjfnb'


if b_count == 0 or  b_count - len(set(b)) > 1 or a_count - b_count > 1:
    print('cslnb')
else:
    print(resh())



