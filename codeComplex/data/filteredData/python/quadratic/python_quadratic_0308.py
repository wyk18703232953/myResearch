import random

def main(n):
    # 生成测试数据：随机 k 和数组 arr
    # 约束：1 <= k <= n，arr 为长度为 n 的随机整数数组
    k = random.randint(1, n)
    arr = [random.randint(-1000, 1000) for _ in range(n)]

    ans = 0.0
    for i in range(n):
        val = arr[i]
        c = 1
        sol = 0.0
        if c >= k:
            sol = max(sol, val / c)
        for j in range(i + 1, n):
            val += arr[j]
            c += 1
            if c >= k:
                sol = max(sol, val / c)
        ans = max(sol, ans)

    print(ans)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n 的大小
    main(10)