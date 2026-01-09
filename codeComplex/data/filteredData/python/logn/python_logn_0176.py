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
    # 生成测试数据：给定规模 n，构造一个与原逻辑兼容的 (n, k)
    # 这里令原始输入的第一个数为 n+1，第二个数为 k+1，其中 k = n
    # 即模拟原始输入: (n+1, n+1)
    k = n

    # 以下逻辑与原 main 完全一致，只是用构造出的 n, k
    n -= 1
    k -= 1
    if n == 0:
        minSplitters = 0
    elif n <= k:
        minSplitters = 1
    elif n > sum_consecutive(k):
        minSplitters = -1

    else:
        minSplitters = min_splitters(n, k)

    # print(minSplitters)
    pass
if __name__ == '__main__':
    # 示例：调用 main，规模可自行调整
    main(10)