import random

def main(n: int) -> int:
    # 1. 生成规模为 n 的测试数据
    #    原代码中 r 的取值范围为 1..10^5
    MAXV = 10**5
    mod = 10**9 + 7

    # 随机生成 n 个数，范围 1..MAXV
    r = [random.randint(1, MAXV) for _ in range(n)]

    # 2. 原逻辑
    dp = [0] * (MAXV + 1)   # 保留原 dp 数组（虽然未使用）
    cnt = [0] * (MAXV + 1)
    tmp = [0] * (MAXV + 1)

    # 统计每个值出现次数
    for x in r:
        cnt[x] += 1

    # 统计每个 i 的倍数中出现的总次数（cnt[i] += cnt[j]）
    for i in range(1, MAXV + 1):
        for j in range(2 * i, MAXV + 1, i):
            cnt[i] += cnt[j]
        tmp[i] = pow(2, cnt[i], mod) - 1

    # 容斥处理
    for i in range(MAXV, 0, -1):
        for j in range(2 * i, MAXV + 1, i):
            tmp[i] = (tmp[i] - tmp[j]) % mod

    # 原程序输出 tmp[1] % mod
    return tmp[1] % mod

# 需要直接运行测试时可取消下面注释，例如 main(5)
# if __name__ == "__main__":
#     print(main(5))