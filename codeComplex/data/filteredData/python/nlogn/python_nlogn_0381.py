import random

def main(n):
    # 生成测试数据：n 个元素，随机 k，随机 pwr 和 cns
    # k 表示最多保留的前面元素数量（原代码里是 k）
    if n <= 0:
        return
    k = random.randint(0, max(0, n - 1))
    # pwr 和 cns 的取值范围可以按需调整
    pwr_list = [random.randint(1, 100) for _ in range(n)]
    cns_list = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    l = sorted(zip(pwr_list, cns_list, range(n)))
    h = []
    sm = 0
    ans = {}

    for i in range(n):
        pwr, cns, ind = l[i]
        sm += cns
        if len(h) > k:
            p = 0
            for j in range(len(h)):
                if h[p] > h[j]:
                    p = j
            sm -= h.pop(p)
        ans[ind] = sm
        h.append(cns)

    # 输出结果
    for i in range(n):
        print(ans[i], end=' ')
    print()

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)