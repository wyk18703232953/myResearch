import random

def combinations(arr, n):
    if n == 0:
        return [[]]
    res = []
    for i in range(len(arr)):
        m = arr[i]
        rem = arr[i + 1:]
        for j in combinations(rem, n - 1):
            res.append([m] + j)
    return res

def solve(arr, n, l, r, x):
    subset = []
    for i in range(2, n + 1):
        for j in combinations(arr, i):
            s = sum(j)
            if l <= s <= r:
                subset.append(j)
    count = 0
    for i in subset:
        mn = min(i)
        mx = max(i)
        if mx - mn >= x:
            count += 1
    return count

def main(n):
    # 生成测试数据
    # n: 数组长度
    # 元素范围、l、r、x 的生成策略可按需调整
    random.seed(0)
    arr = [random.randint(1, 20) for _ in range(n)]
    l = random.randint(1, 10 * n)
    r = random.randint(l, 15 * n)
    x = random.randint(0, 10)

    # 执行原逻辑
    ans = solve(arr, n, l, r, x)
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(5)