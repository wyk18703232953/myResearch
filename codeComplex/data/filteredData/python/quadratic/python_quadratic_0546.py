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
    # 生成长度为 n 的确定性字符串 s
    # 奇数位置为 '+', 偶数位置为 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    ans = 99999999
    for i in range(n + 1):
        stones = stones_after(i, s)
        if stones != -1:
            ans = min(ans, stones)
    print(ans)

if __name__ == "__main__":
    # 示例：将 n 视为字符串长度
    main(10)