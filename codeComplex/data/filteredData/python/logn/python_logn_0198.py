def digitsum(n):
    init = 0
    for item in str(n):
        init += int(item)
    return init

def solve_single_case(n, s):
    if n - digitsum(n) < s:
        return 0
    i = 0
    j = n
    while i < j:
        mid = (i + j) // 2
        if mid - digitsum(mid) < s:
            i = mid + 1

        else:
            j = mid
    return n - i + 1

def main(n):
    # 将 n 映射为原程序中的 (N, S)
    # 使得规模随 n 增大且生成方式确定
    N = max(1, n * 1000)
    S = max(0, n // 2)
    result = solve_single_case(N, S)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)