def main(n):
    """
    将原程序改为无 input() 版本：
    - n 作为“规模”参数，这里解释为：生成 n 组 (n_i, k_i) 测试数据并依次处理。
    - 测试数据生成策略可按需要修改，这里给出一个简单示例：
        对第 i 组数据：
            n_i = i + 1
            k_i = 1 + (i * 3)  # 使 k 随 i 增长
    """
    results = []

    for i in range(n):
        # 生成一组测试数据 (n_i, k_i)
        ni = i + 1
        ki = 1 + i * 3

        # 原逻辑开始
        if (ni == 2 and ki == 3) or (ni <= 30 and ki > (4 ** ni - 1) // 3):
            results.append("NO")
        else:
            cn = ni - 1
            ck = ki - 1
            l = 1
            while cn * ck != 0 and ck >= 4 * l - 1:
                ck -= 4 * l - 1
                cn -= 1
                l *= 2
            results.append(f"YES {cn}")

    # 输出所有结果
    print("\n".join(results))


if __name__ == "__main__":
    # 示例：运行规模 n = 5
    main(5)