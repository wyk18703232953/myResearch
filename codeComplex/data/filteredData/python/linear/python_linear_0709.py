import random

def main(n):
    # 根据规模 n 生成由 '+' 和 '-' 组成的长度为 n 的测试字符串
    # 这里简单设定每个位置 50% 概率为 '+'，50% 概率为 '-'
    s = ''.join(random.choice(['+', '-']) for _ in range(n))

    t = 0
    for ch in s:
        if ch == '+':
            t += 1
        else:
            t = max(t - 1, 0)

    print(max(t, 0))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)