n = 0  # placeholder to satisfy linter; real n comes from main(n)

def main(n):
    # 生成长度为 n 的确定性字符串 s，由 '+' 和 '-' 组成
    # 规则：i 偶数为 '+', i 奇数为 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    maxn = 0
    now = 0
    for i in s:
        if i == '+':
            now += 1

        else:
            now -= 1
        maxn = max(maxn, -now)
    result = now + maxn
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)