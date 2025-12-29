import random

def main(n: int):
    # 生成测试数据
    # 随机生成数组 arr，长度为 n，元素在 [1, 2*n] 范围内
    arr = [random.randint(1, 2 * n) for _ in range(n)]
    # 从 arr 中任选一个元素作为 m，确保 m 一定在数组中
    m = random.choice(arr)

    # 原逻辑开始
    ma = {0: 1}
    s, fla, ans = 0, False, 0
    for v in arr:
        if v == m:
            fla = True
        elif v < m:
            s -= 1
        elif v > m:
            s += 1
        if fla:
            ans += ma.get(s, 0) + ma.get(s - 1, 0)
        else:
            ma[s] = ma.get(s, 0) + 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)