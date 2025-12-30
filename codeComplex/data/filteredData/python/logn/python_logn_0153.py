def sum_1(n):
    s = n * (n + 1) // 2
    return s

def sum_2(s, e):
    if s <= 1:
        return sum_1(e)
    return sum_1(e) - sum_1(s - 1)

def mini_splitter(k, n):
    st = 1
    end = k
    while st < end:
        mid = (st + end) // 2
        s = sum_2(mid, k)
        if s == n:
            return k - mid + 1
        elif s > n:
            st = mid + 1
        else:
            end = mid
    return k - st + 2

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里将 n 视为原程序中的 n，并构造一个合理的 k。
    # 例如让 k = n（或更大）用来测试一般情况。
    k = max(1, n)

    if n == 1:
        print("0")
    elif n <= k:
        print("1")
    else:
        k -= 1
        n -= 1
        if sum_1(k) < n:
            print("-1")
        else:
            print(mini_splitter(k, n))

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)