from bisect import bisect
import random

def main(n):
    # 生成测试数据
    # n: 数组 vv 的大小，同时也作为操作次数 m 的规模基础
    #
    # 生成 n 个递增的正整数作为 vv
    # vv 中的值分布在 [1, 10^9] 范围内
    vv = sorted(random.randint(1, 10**9) for _ in range(n))

    # 生成 m 条操作，这里令 m 与 n 同规模；可按需调整比例
    m = n
    ops = []
    for _ in range(m):
        one = 1  # 原代码只在 one == 1 时有逻辑，其它值无效果
        # 随机生成 x，范围与 vv 一致（含 10^9，用于触发特殊分支）
        x = random.randint(1, 10**9)
        dummy = 0  # 第三个参数在原代码中未使用
        ops.append((one, x, dummy))

    # 下面是原逻辑，只是用生成的 vv、ops 来代替 input()

    hh = [0] * n
    rr = 0

    for one, x, _ in ops:
        if one == 1:
            if x == 1000000000:
                rr += 1
            else:
                ind = bisect(vv, x)
                if ind:
                    hh[ind - 1] += 1

    r = n
    s = 0
    for i, h in reversed(list(enumerate(hh))):
        s += h
        r = min(r, s + i)

    ans = r + rr
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：以 n = 10 运行一遍
    main(10)