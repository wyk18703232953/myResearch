import random

def f(ch):
    return 0 if ch == '0' else 1

def main(n):
    # 生成测试数据：长度为 n 的两行由 '0'/'1' 组成的字符串
    s1 = ''.join(random.choice('01') for _ in range(n))
    s2 = ''.join(random.choice('01') for _ in range(n))

    U = [
        [f(i) for i in s1],
        [f(i) for i in s2]
    ]

    i = 0
    size = len(U[0])
    ans = 0

    while i + 1 < size:
        s = U[0][i] + U[0][i + 1] + U[1][i] + U[1][i + 1]
        if s > 1:
            i += 1
            continue
        elif s == 1:
            U[0][i] = U[0][i + 1] = U[1][i] = U[1][i + 1] = 1
            ans += 1
        else:
            U[0][i] = 1
            U[0][i + 1] = 1
            U[1][i] = 1
            ans += 1
        i += 1

    print(ans)

if __name__ == "__main__":
    # 示例调用：n 为规模
    main(10)