import random

def main(n: int):
    # 生成长度为 n 的随机字符串，仅包含 'H' 和 'T'
    s = ''.join(random.choice('HT') for _ in range(n))

    hc = s.count('H')
    tc = s.count('T')

    # 边界情况：如果全是 H 或全是 T，则无需翻转
    if hc == 0 or tc == 0:
        print(0)
        return

    # 原逻辑：滑动窗口统计
    hr = min(s[i:i + hc].count('T') for i in range(n - hc + 1))
    tr = min(s[i:i + tc].count('H') for i in range(n - tc + 1))

    print(min(hr, tr))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)