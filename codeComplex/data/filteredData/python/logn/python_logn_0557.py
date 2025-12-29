import bisect
import random


def main(n):
    # n 作为“规模”，这里用来生成一个不超过 n 的随机 k
    # 若希望固定 k，可直接把 k 赋为某个常数
    if n <= 0:
        return

    # 构造与原程序相同的表 b, a
    b = [0]
    for i in range(1, 15):
        b.append(9 * i * (10 ** (i - 1)))

    a = [b[0]]
    for i in range(1, 15):
        a.append(a[i - 1] + b[i])

    # 生成测试数据：k ∈ [1, min(n, a[-1])]
    max_k = min(n, a[-1])
    if max_k < 1:
        return
    k = random.randint(1, max_k)

    # 以下为原逻辑，仅将除法改为整除，避免浮点问题
    th = bisect.bisect_left(a, k)
    th -= 1
    k = k - a[th]
    start = 10 ** th
    now = th + 1
    rem = k % now
    iss = k // now
    end = start + (k // now)
    temp = str(end - 1)
    s = ""
    s += temp[now - 1] + str(end) + str(end + 1)

    print(s[rem])


if __name__ == "__main__":
    # 示例：用 n = 10^12 作为规模
    main(10 ** 12)