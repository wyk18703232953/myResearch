def validation(n, k, x):
    s = (x * (x + 1)) // 2 - (n - x)
    if s == k:
        return 0
    if s > k:
        return 1
    return 2

def main(n):
    # 将规模 n 映射为原程序的两个输入 n, k
    # 原程序只有一组输入 (n, k)，这里设定：
    # n_original = n
    # k_original = n * (n + 1) // 4  （确定性构造，保证随 n 规模变化）
    n_original = n
    k_original = (n_original * (n_original + 1)) // 4

    l = 0
    r = 1000000001
    ans = 0
    while True:
        mid = (l + r) // 2
        flag = validation(n_original, k_original, mid)
        if flag == 0:
            ans = mid
            break
        elif flag == 1:
            r = mid

        else:
            l = mid

    result = n_original - ans
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)