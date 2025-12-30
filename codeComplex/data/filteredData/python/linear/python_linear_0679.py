import sys
import random

sys.setrecursionlimit(1000000)


def main(n):
    # 生成测试数据 zb，满足原算法中对 zb 的隐含约束
    # 原逻辑会构造一条长度为 N 的序列 zr，前后对称，与 zb 的关系为：
    # zb[i] = za1[i] + za2[i]，其中 za1 非减，za2 非增，且 za1[0] = 0, za2[0] = zb[0]
    #
    # 为了保证算法不触发 assert False，我们反推构造一个合法的 zr，然后由它生成 zb。
    #
    # 具体做法：
    # 1. 构造一个长度为 N 的非减序列 zr。
    # 2. 令 za1 为 zr 的前半段，za2 为 zr 的后半段的镜像。
    # 3. zb[i] = za1[i] + za2[i]。

    if n % 2 != 0:
        # 原代码只在 range(1, N//2) 上循环，并构造长度为 N 的对称序列，
        # 因此 N 需要是偶数，这里强制调整为偶数。
        n += 1

    # 构造一个非减的 zr
    zr = [0]
    for _ in range(1, n):
        # 每一步增加一个非负随机增量，保证非减
        zr.append(zr[-1] + random.randint(0, 5))

    # 由 zr 构造 za1, za2
    half = n // 2
    za1 = zr[:half]
    za2 = zr[half:][::-1]  # 后半段反向

    # 构造 zb
    zb = [za1[i] + za2[i] for i in range(half)]

    # ========= 以下为原逻辑 =========
    N = n  # 与原变量名保持一致

    za1_calc = [0]
    za2_calc = [zb[0]]

    for i in range(1, N // 2):
        t1 = zb[i] - za1_calc[-1]
        if t1 <= za2_calc[-1]:
            za1_calc.append(za1_calc[-1])
            za2_calc.append(t1)
            continue
        t2 = zb[i] - za2_calc[-1]
        if t2 >= za1_calc[-1]:
            za1_calc.append(t2)
            za2_calc.append(za2_calc[-1])
            continue
        # 按原程序，如果两种情况都不满足，就认为输入非法
        raise AssertionError("Constructed zb violated constraints")

    zr_calc = za1_calc + za2_calc[::-1]
    zs = [str(x) for x in zr_calc]
    r = ' '.join(zs)
    print(r)


if __name__ == "__main__":
    # 示例：可以在这里给一个默认规模
    main(10)