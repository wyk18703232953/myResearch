import random

def main(n: int) -> None:
    # 1. 生成规模为 n 的测试数据：两行由 '0' / '1' 组成的字符串
    # 可按需要调整生成策略，这里采用随机生成
    b = []
    for _ in range(2):
        row = [random.choice(['0', '1']) for _ in range(n)]
        b.append(row)

    # 2. 原逻辑
    ans = 0
    a = []
    for i in range(n):
        ai = 0
        if b[0][i] == '0':
            ai += 1
        if b[1][i] == '0':
            ai += 1
        a.append(ai)

    prv = 0
    for i in range(n):
        if a[i] == 0:
            prv = 0
        elif a[i] == 1:
            if prv == 2:
                ans += 1
                prv = 0
            else:
                prv = 1
        elif a[i] == 2:
            if prv == 2:
                ans += 1
                prv = 1
            elif prv == 1:
                ans += 1
                prv = 0
            else:
                prv = 2

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)