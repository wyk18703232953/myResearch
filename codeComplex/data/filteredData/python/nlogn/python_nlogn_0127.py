import random

def solve_instance(n, m, k, a):
    a.sort(reverse=True)
    if k >= m:
        return 0
    curr = k
    count = 0
    for i in range(n):
        curr += a[i] - 1
        count += 1
        if curr >= m:
            break
    if curr >= m:
        return count
    else:
        return -1

def main(n):
    # 生成测试数据
    # 约束可根据需要调整
    if n <= 0:
        return

    # 随机生成 m, k 和数组 a
    # 保证 1 <= k <= m，a[i] >= 1
    m = random.randint(1, n * 10 + 1)
    k = random.randint(0, m)
    a = [random.randint(1, 10) for _ in range(n)]

    ans = solve_instance(n, m, k, a)
    print(n, m, k)
    print(" ".join(map(str, a)))
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的测试数据并求解
    main(5)