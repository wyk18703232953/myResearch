def main(n):
    # 原程序输入结构：
    # 第一行：n, q
    # 接下来 q 组：
    #   整数 u
    #   字符串 s
    #
    # 在这里我们固定：
    #   n 为函数参数
    #   q = n
    #   第 i 组：
    #       u_i = i + 1
    #       s_i 为长度 i+1 的指令串，由 'L','R','U' 组成，按循环模式 "LRU" 生成
    #
    # 这样规模 n 同时控制：
    #   - 测试组数 q
    #   - 每组字符串长度为 O(n)
    #
    # 若原始算法对过大 n 不适合，可以在外层调用时自行控制 n 的上限
    q = n

    # 为了保持与原逻辑一致，用一个内部函数模拟原主逻辑（针对单个 u, s）
    def process_single(u, s, n_limit):
        for comm in s:
            k = 1
            while True:
                if k & u:
                    break
                k <<= 1
            if comm == 'L':
                if k != 1:
                    u -= k
                    u += (k >> 1)
            elif comm == 'R':
                if k != 1:
                    u += (k >> 1)
            elif comm == 'U':
                nu = u - k
                nu |= (k << 1)
                if nu <= n_limit:
                    u = nu
        return u

    results = []
    for i in range(q):
        u = i + 1  # 确定性生成 u
        # 生成指令串：长度为 i+1，按 "LRU" 循环
        pattern = "LRU"
        length = i + 1
        s_chars = [pattern[j % 3] for j in range(length)]
        s = "".join(s_chars)
        res = process_single(u, s, n)
        results.append(res)

    # 为了方便时间复杂度实验，返回结果列表
    return results


if __name__ == "__main__":
    # 示例：运行规模为 10
    out = main(10)
    for v in out:
        print(v)