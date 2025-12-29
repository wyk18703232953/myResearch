def arithmetic_sum(length, r):
    # 等差数列求和：长度为 length，末项为 r，公差为 1（即 r-length+1 到 r）
    return length * (2 * r - (length - 1)) // 2

def search_function(total, l, r):
    left = l
    right = r

    while left <= right:
        mid = (right + left) // 2
        length = r - mid + 1
        result = arithmetic_sum(length, r)

        if result == total:
            return length
        elif result > total:
            left = mid + 1
        else:
            length_plus = length + 1
            if arithmetic_sum(length_plus, r) > total:
                return length_plus
            else:
                right = mid - 1
    return -1

def solve_single_case(n, m):
    # 原逻辑中先读 n, m，然后做 n -= 1, m -= 1
    n -= 1
    m -= 1

    if n == 0:
        return 0
    elif arithmetic_sum(m, m) < n:
        return -1
    elif m < n:
        return search_function(n, 1, m)
    else:
        return 1

def generate_test_case(n):
    """
    根据规模 n 生成测试数据 (n, m)。
    这里简单设定 m = n 或 m = max(1, n//2) 等都可以。
    选择 m = n，保证规模与 n 同阶。
    """
    m = n
    return n, m

def main(n):
    """
    n 为规模参数，用于生成测试数据并执行原逻辑。
    返回结果值（原程序是直接打印）。
    """
    N, M = generate_test_case(n)
    result = solve_single_case(N, M)
    print(result)

# 示例：直接调用 main(10) 运行一次
if __name__ == "__main__":
    main(10)