import random

def main(n: int):
    # 生成规模为 n 的测试数据（这里生成 n 个随机整数）
    # 可根据需要自行调整数据生成策略
    x = [random.randint(-10**9, 10**9) for _ in range(n)]

    x.sort()
    s = set(x)
    m, ans = 1, [x[0]]
    pow2 = [1]
    for _ in range(35):
        pow2.append(2 * pow2[-1])

    for i in x:
        for j in pow2:
            if (i - j) in s and (i + j) in s:
                m = 3
                ans = [i - j, i, i + j]
                break
            elif (i - j) in s and m < 2:
                m = 2
                ans = [i, i - j]
            elif (i + j) in s and m < 2:
                m = 2
                ans = [i, i + j]
        if m == 3:
            break

    print(m)
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)