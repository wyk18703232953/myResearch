import math

def main(n):
    # 生成确定性的 k，与 n 存在合理关系以覆盖多种分支
    if n <= 0:
        return
    # 让 k 在 1 到 3n 之间循环，避免为 0
    k = (2 * n) % (3 * n)
    if k == 0:
        k = 1

    if n == k:
        # print(math.ceil(n / 2) - 1)
        pass
    elif k > 2 * n:
        # print(0)
        pass

    else:
        # print(min(n, k - 1) - k // 2)
        pass
if __name__ == "__main__":
    main(10)