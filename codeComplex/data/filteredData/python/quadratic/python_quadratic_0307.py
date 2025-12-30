import random

def helper(n, k, l):
    res = 0.0
    for i in range(n - k + 1):
        base_seg = l[i:i + k]
        sm_bseg = sum(base_seg)
        ln_bseg = len(base_seg)
        ans = sm_bseg / ln_bseg

        for j in range(i + k, n):
            sm_bseg += l[j]
            ln_bseg += 1
            ans = max(ans, sm_bseg / ln_bseg)

        res = max(res, ans)

    return res

def main(n):
    # 生成测试数据：n 个整数，范围可按需调整
    # 保证 1 <= k <= n
    l = [random.randint(-1000, 1000) for _ in range(n)]
    k = random.randint(1, n)
    result = helper(n, k, l)
    print(result)

if __name__ == "__main__":
    # 示例：规模为 10，可按需修改
    main(10)