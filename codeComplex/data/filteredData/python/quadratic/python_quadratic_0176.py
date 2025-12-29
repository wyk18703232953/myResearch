import random

def main(n):
    # 生成测试数据：n 和 k，以及长度为 n 的 ns 列表
    # 这里示例设置 k 在 [1, 10] 范围内，ns[i] 在 [0, 255] 范围内
    k = random.randint(1, 10)
    ns = [random.randint(0, 255) for _ in range(n)]

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
                if kk + j >= 256 or (done[kk + j] is not None and done[kk + j] != -1):
                    break
                if kk + j <= c:
                    done[kk + j] = j
                else:
                    done[kk + j] = -1
        elif done[c] == -1:
            j = c
            while True:
                if done[j] is not None and done[j] != -1:
                    break
                j -= 1
            a = done[j]
            for kk in range(j, c + 1):
                done[kk] = a
        else:
            pass
        ans[i] = done[c]

    ans = [str(x) for x in ans]
    print(' '.join(ans))


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次运行
    main(10)