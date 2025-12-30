import random

def main(n):
    # 生成测试数据
    # n: 数组 a 的长度
    # m: 数组 b 的长度，这里设为 n 或 n+1，保证 m >= 1 且可变
    m = n + 1 if n > 1 else 1

    # 生成数组 a 和 b 的测试数据（正整数）
    # 保证有一定范围，避免溢出；可以按需修改生成规则
    a = [random.randint(1, 10**6) for _ in range(n)]
    b = [random.randint(1, 10**6) for _ in range(m)]

    # 原逻辑开始
    a.sort()
    b.sort()
    a.reverse()
    b.reverse()

    if a[0] > b[-1]:
        print(-1)
    else:
        flag = True
        if b[-1] == a[0]:
            s = sum(b)
            flag = False
        else:
            s = sum(b) - b[-1] + a[0]
        if flag:
            s += (sum(a) - a[0]) * m + b[-1] - a[1]
        else:
            s += (sum(a) - a[0]) * m
        print(s)

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)