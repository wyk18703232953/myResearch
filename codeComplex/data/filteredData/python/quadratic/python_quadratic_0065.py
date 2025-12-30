import random

def main(n: int):
    # 1) 生成测试数据
    # 生成一个长度为 n 的随机整数数组，元素范围可按需调整
    nums = [random.randint(0, 100) for _ in range(n)]

    # 生成随机查询次数 m（1 到 n 之间）
    m = random.randint(1, n) if n > 0 else 0
    queries = []
    for _ in range(m):
        if n == 0:
            break
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 2) 计算初始逆序对个数的奇偶性
    counts = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                counts += 1
    ans = counts % 2

    # 3) 按查询更新并记录结果
    ans_tmp = []
    for (l, r) in queries:
        tmp = r - l + 1
        tmp_count = tmp * (tmp - 1) // 2
        if tmp_count % 2 == 1:
            ans = (ans + 1) % 2
        ans_tmp.append(ans)

    # 4) 输出结果
    for ans in ans_tmp:
        if ans % 2 == 1:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时按需修改 n
    main(5)