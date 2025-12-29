def sum_from1(k):
    return (k * (k + 1)) // 2

def sum_of_subtraction(p, k):
    if p <= 1:
        return sum_from1(k)
    else:
        return sum_from1(k) - sum_from1(p - 1)

def solve(n, k):
    if n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        n -= 1
        k -= 1
        if n > sum_from1(k):
            return -1
        else:
            s = 1
            e = k
            while s < e:
                mid = (s + e) // 2
                r = sum_of_subtraction(mid, k)
                if r == n:
                    return k - mid + 1
                elif r > n:
                    s = mid + 1
                else:
                    e = mid
            else:
                return k - s + 2

def main(n):
    # 根据规模 n 生成测试数据 (n, k)
    # 这里简单设定 k = n，保证有一定规模的搜索空间
    k = n
    ans = solve(n, k)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)