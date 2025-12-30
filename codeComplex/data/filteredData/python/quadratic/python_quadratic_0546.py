def stones_after(n, s):
    for ch in s:
        if ch == '-':
            n -= 1
        else:
            n += 1
        if n < 0:
            return -1
    return n

def main(n):
    # 生成长度为 n 的测试串，这里简单生成交替的 '+' 和 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    ans = 99999999
    for i in range(n + 1):
        stones = stones_after(i, s)
        if stones != -1:
            ans = min(ans, stones)
    print(ans)