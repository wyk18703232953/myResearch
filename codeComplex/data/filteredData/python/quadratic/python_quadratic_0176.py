def main(n):
    # 映射含义：
    # n = 输入数组 ns 的长度
    # k = 一个与 n 相关且可扩展的窗口大小，保持确定性
    if n <= 0:
        # print("")
        pass
        return

    # 规模化且确定性的 k：保证 1 <= k <= 256
    # 这里让 k 随 n 增长，但不超过 256
    k = max(1, min(256, n // 2 if n >= 2 else 1))

    # 生成确定性的 ns，元素范围在 [0, 255] 内
    # 使用简单算术构造，避免随机性
    ns = [((i * 37 + 13) % 256) for i in range(n)]

    done = [None] * 256
    ans = [None] * n

    for i in range(n):
        c = ns[i]
        if done[c] is None:
            j = c
            while True:
                if j < 0 or c - j >= k or (done[j] is not None and done[j] != -1):
                    break
                j -= 1
            j += 1
            for kk in range(k):
                idx = kk + j
                if idx >= 256 or (done[idx] is not None and done[idx] != -1):
                    break
                if idx <= c:
                    done[idx] = j

                else:
                    done[idx] = -1
        elif done[c] == -1:
            j = c
            while True:
                if done[j] is not None and done[j] != -1:
                    break
                j -= 1
            a = done[j]
            for kk in range(j, c + 1):
                done[kk] = a
        ans[i] = done[c]

    ans_str = [str(x) for x in ans]
    # print(" ".join(ans_str))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 来进行规模化实验
    main(10)