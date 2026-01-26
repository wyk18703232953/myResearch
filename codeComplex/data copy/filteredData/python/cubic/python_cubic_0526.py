import bisect

ls2int = lambda ls: int(''.join(map(str, ls)))

def candidates(digs, num):
    if not digs:
        return [[]]
    res = []
    i = bisect.bisect_left(digs, num[0])
    if num[0] in digs:
        for suffix in candidates(digs[:i] + digs[i+1:], num[1:]):
            res.append([digs[i]] + suffix)
    if i > 0:
        i -= 1
        res.append([digs[i]] + list(reversed(digs[:i] + digs[i+1:])))
    return res

def solution(a, b):
    digits = [int(x) for x in sorted(a)]
    ceiling = [int(x) for x in b]
    assert len(digits) <= len(ceiling), 'solution does not exist'
    if len(digits) < len(ceiling):
        return ls2int(digits[::-1])
    return max(ls2int(ls) for ls in candidates(digits, ceiling))

def main(n):
    if n <= 0:
        n = 1
    # 生成长度为 n 的字符串 a，由 0-9 周期数字构成
    a = ''.join(str(i % 10) for i in range(n))
    # 生成长度为 n 或 n+1 的字符串 b，保证 len(a) <= len(b)
    if n % 2 == 0:
        # 同长度，首位为 1 以避免前导 0 的极端情况
        b = '1' + ''.join(str((i * 2 + 3) % 10) for i in range(n - 1))

    else:
        # 长度比 a 多 1，首位为 1，其余为简单算术生成
        b = '1' + ''.join(str((i * 3 + 1) % 10) for i in range(n))
    result = solution(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)