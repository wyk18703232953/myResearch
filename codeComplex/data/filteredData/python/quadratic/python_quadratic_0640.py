import random

def main(n: int):
    # 生成测试数据：n 个 1~10^9 之间的随机整数
    # 可以根据需要调整数据生成策略
    arr = [random.randint(1, 10**9) for _ in range(n)]

    a = sorted(list(set(arr)))
    m = len(a)
    used = [0] * m
    cnt = 0
    for i in range(m):
        if not used[i]:
            used[i] = 1
            cnt += 1
            for j in range(i + 1, m):
                if a[j] % a[i] == 0:
                    used[j] = 1
    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改规模
    main(10)