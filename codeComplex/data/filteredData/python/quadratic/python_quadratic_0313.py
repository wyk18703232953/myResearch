import math

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 998244353
EPS = 1e-6

def main(n):
    # 映射 n 为原程序中的 n，k
    if n < 2:
        n_eff = 2

    else:
        n_eff = n
    k = max(1, n_eff // 2)

    # 生成长度为 n_eff 的确定性数组 a
    # 使用简单算术构造，确保非负且有变化
    a = [(i * 7 + 3) % 1000 for i in range(n_eff)]

    ans = 0.0

    for i in range(n_eff - k + 1):
        num = sum(a[i:i + k])
        den = k
        ans = max(ans, num / den)

        for j in range(i + k, n_eff):
            num += a[j]
            den += 1
            ans = max(ans, num / den)

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行时间复杂度实验
    main(10)