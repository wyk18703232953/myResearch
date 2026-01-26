def main(n):
    # 解释：
    # 原程序从输入读取 n, k，这里将 n 作为规模参数，同时生成确定性的 k。
    # 为了保持结构合理，令 k 与 n 有确定关系，比如 k = n // 2 + 1。
    # 这样对于同一 n，每次运行生成的 (n, k) 都相同，算法逻辑不变。

    k = n // 2 + 1  # 确定性构造 k

    cand = 0
    tot = 0
    p = 0
    # 保持原有循环逻辑，只是去掉 input 依赖
    while tot < k or tot - (n - p) != k:
        cand += 1
        tot += cand
        p += 1

    result = tot - k
    print(result)
    return result


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模进行一次调用
    main(10)