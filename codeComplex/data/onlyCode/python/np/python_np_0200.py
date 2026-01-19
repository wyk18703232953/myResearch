def solve():
    n, l, r, x = map(int, input().split(' '))
    c = list(map(int, input().split(' ')))
    ans = 0
    for bitmask in range(2 ** n):
        if bin(bitmask).count('1') > 1:
            res, _min, _max = 0, float('+inf'), float('-inf')
            for c_i, bit_i in zip(c, (1 & int(bitmask) >> i for i in range(n))):
                if bit_i:
                    res += c_i * bit_i
                    if c_i < _min:
                        _min = c_i
                    if c_i > _max:
                        _max = c_i
            if l <= res <= r and (_max - _min) >= x:
                ans += 1
    print(ans)
            

if __name__ == '__main__':
    solve()