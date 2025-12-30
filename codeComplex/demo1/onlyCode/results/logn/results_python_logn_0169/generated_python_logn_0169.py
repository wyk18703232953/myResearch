def main(n):
    # 自动生成与规模 n 相关的测试数据 k
    # 这里选择一个与 n 同阶的 k，保证有较大概率存在解
    # 同时 k 至少为 2
    k = max(2, n)  # 可根据需要调整生成策略

    # 原逻辑开始（去除 input()，使用上面生成的 n, k）

    ini, fin = 1, k - 1
    if n == 1:
        print("0")
        return

    if 1 + (k * (k - 1)) // 2 < n:
        print("-1")
        return

    while ini < fin:
        mid = (ini + fin) // 2
        s = 1 + (k - 1) * mid - (mid * (mid - 1)) // 2
        if s >= n:
            fin = mid
        else:
            ini = mid + 1

    print(ini)


if __name__ == "__main__":
    # 示例：调用 main(n) 进行测试
    # 可根据需要修改 n 的取值
    main(10)