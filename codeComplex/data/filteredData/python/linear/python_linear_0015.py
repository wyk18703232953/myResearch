import math

def main(n):
    # 由 n 确定性生成原程序需要的 n, k
    # 约束：原程序中质数枚举从 2 到 n-1，所以 n 至少为 3
    if n < 3:
        n_val = 3
    else:
        n_val = n
    # 让 k 随规模线性变化但保持确定性
    # 至少为 1，最大不超过  n_val // 2  以保证有一定概率满足条件
    k_val = max(1, n_val // 4)

    l = []
    c = 0
    for j in range(2, n_val):
        p = 0
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                p = 1
                break
            else:
                pass
        if p == 0:
            l.append(j)

    l += [n_val]

    for i in range(len(l) - 1):
        if (l[i] + l[i + 1] + 1) in l:
            c += 1

    if c >= k_val:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用，可根据需要修改不同的 n 进行实验
    main(10)