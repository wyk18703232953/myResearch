def main(n):
    # 预处理 f 数组，与原代码一致
    f = [0 for _ in range(40)]
    for i in range(1, 32):
        f[i] = 1 + 4 * f[i - 1]

    # 按规模 n 生成测试数据：
    # 这里生成 t = n 组 (n_i, k_i) 测试：
    # n_i 从 1 到 n（若 n > 40，则截断到 40），
    # k_i 为 1 到 f[n_i] + 2 的某种值（这里简单设为 f[n_i] // 2 + 1）。
    t = n
    queries = []
    for i in range(1, t + 1):
        ni = i
        if ni > 40:
            ni = 40
        # 对于 n_i >= 32 时，f[n_i] 实际不会用到，k 随便给一个较大值
        if ni < 32:
            ki = f[ni] // 2 + 1  # 中等大小的 k

        else:
            ki = 10**18
        queries.append((ni, ki))

    # 按原逻辑处理 queries
    for n_val, k in queries:
        if n_val >= 32:
            # print("YES %d" % (n_val - 1))
            pass
            continue

        if f[n_val] < k:
            # print("NO")
            pass
            continue

        k -= 1
        extra = 1
        way = 3
        size = n_val - 1
        total = f[size]
        ans = True

        while k > total and size > 0:
            if k < way:
                ans = False
                break
            k -= way
            size -= 1
            extra = way * 2 - 1
            way = way * 2 + 1
            total += extra * f[size]

        if ans:
            # print("YES %d" % size)
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)