def really_big(x, s):
    sum_digit = 0
    digits = x
    while digits > 0:
        sum_digit += digits % 10
        digits = digits // 10

    if x - sum_digit >= s:
        return True
    return False

def solve(n, s):
    left = 1
    right = n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if really_big(mid, s):  # mid is really big
            right = mid - 1
            ans = n - mid + 1
        else:  # mid is not really big
            left = mid + 1
    return ans

def main(n):
    # 映射规则：
    # 使用 n 作为原程序中的 n
    # 使用一个确定性的 s，与 n 存在固定关系
    # 例如：s = max(1, n // 2)
    original_n = n
    original_s = max(1, n // 2)
    result = solve(original_n, original_s)
    # print(result)
    pass
if __name__ == "__main__":
    main(25)