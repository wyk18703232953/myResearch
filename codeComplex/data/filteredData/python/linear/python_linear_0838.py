def main(n):
    # n 作为规模参数：构造 Q 组数据，每组字符串长度为 n，窗口大小为 K = max(1, n // 2)
    Q = max(1, n)
    K = max(1, n // 2)
    D = {"R": 0, "G": 1, "B": 2}
    chars = ["R", "G", "B"]

    def build_string(length, offset):
        # 构造长度为 length 的确定性 RGB 串
        return "".join(chars[(i + offset) % 3] for i in range(length))

    for q in range(Q):
        # N 随着组号和 n 变化，但总是确定性的，且 N >= 1
        N = max(1, n + q)
        S = build_string(N, q % 3)
        mi = K
        for base in range(3):
            d = 0
            for j in range(N):
                if D[S[j]] != (base + j) % 3:
                    d += 1
                if j >= K and D[S[j - K]] != (base + j - K) % 3:
                    d -= 1
                if j >= K - 1:
                    if d < mi:
                        mi = d
        # print(mi)
        pass
if __name__ == "__main__":
    # 示例调用：可以修改 n 以测试不同规模
    main(10)