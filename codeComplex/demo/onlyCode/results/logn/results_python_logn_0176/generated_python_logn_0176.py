import random

def sum_consecutive(num):
    return int(0.5 * num * (num + 1))


def sum_consecutive2(num1, num2):
    return sum_consecutive(num2) - sum_consecutive(num1 - 1)


def min_splitters(n, k):
    low, high = 1, k
    while low < high:
        mid = (low + high) // 2
        summation = sum_consecutive2(mid, k)
        if summation == n:
            return k - mid + 1
        elif summation > n:
            low = mid + 1
        else:
            high = mid
    return k - low + 2


def main(n):
    # 根据规模 n 生成测试数据：
    # n 表示原始程序中的 n 的“规模上界”
    # 这里生成 1 <= n_val <= n，且 1 <= k_val <= n
    if n < 1:
        raise ValueError("n should be >= 1 for test generation")

    # 生成原始意义上的 n 和 k
    n_val = random.randint(1, n)
    k_val = random.randint(1, n)

    # 按原始程序逻辑：读入的是 (n, k)，然后做 n-=1, k-=1
    n_adj = n_val - 1
    k_adj = k_val - 1

    if n_adj == 0:
        minSplitters = 0
    elif n_adj <= k_adj:
        minSplitters = 1
    elif n_adj > sum_consecutive(k_adj):
        minSplitters = -1
    else:
        minSplitters = min_splitters(n_adj, k_adj)

    print(minSplitters)


if __name__ == '__main__':
    # 示例：使用规模 10 进行测试
    main(10)