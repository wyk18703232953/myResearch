import random

def main(n: int):
    # 生成规模为 n 的测试数据：非负整数序列 m
    # 这里简单生成 0~10 之间的随机整数，可根据需要调整
    m = [random.randint(0, 10) for _ in range(n)]

    t = []
    for i in range(n):
        if i == 0:
            t.append(m[i] + 1)
        else:
            t.append(max(t[i - 1], m[i] + 1))

    s = t[n - 1] - m[n - 1] - 1
    for i in range(n - 2, -1, -1):
        if t[i] < t[i + 1] - 1:
            t[i] = t[i + 1] - 1
        s += t[i] - m[i] - 1

    print(s)

if __name__ == "__main__":
    # 示例：调用 main，规模设为 5
    main(5)