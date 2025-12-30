import random

def validation(n, k, x):
    if (x * (x + 1)) // 2 - (n - x) == k:
        return 0
    if (x * (x + 1)) // 2 - (n - x) > k:
        return 1
    return 2

def main(n):
    # 根据规模 n 生成测试数据
    # 原程序逻辑只依赖于 n 和 k，这里构造一个合理的 k
    # 为保证有解，先随机生成 ans，再由等式反推 k
    ans = random.randint(0, n)
    k = (ans * (ans + 1)) // 2 - (n - ans)

    l = 0
    r = 1000000001
    while True:
        mid = (l + r) // 2
        flag = validation(n, k, mid)
        if flag == 0:
            found_ans = mid
            break
        elif flag == 1:
            r = mid
        else:
            l = mid

    print(n - found_ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)