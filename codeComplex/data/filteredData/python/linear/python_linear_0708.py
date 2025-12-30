import random

def main(n: int):
    # 生成测试数据：长度为 n 的只含 '+' 和 '-' 的字符串
    s = ''.join(random.choice(['+', '-']) for _ in range(n))

    maxn = 0
    now = 0
    for ch in s:
        if ch == '+':
            now += 1
        else:
            now -= 1
        maxn = max(maxn, -now)
    print(now + maxn)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)