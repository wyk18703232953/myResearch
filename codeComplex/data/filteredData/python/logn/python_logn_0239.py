import random

def really_big(x, s):
    sum_digit = 0
    digits = x
    while digits > 0:
        sum_digit += digits % 10
        digits //= 10

    return x - sum_digit >= s

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
    # 根据 n 生成测试数据，这里示例：s 为 [0, n] 范围内的随机数
    s = random.randint(0, n)
    result = solve(n, s)
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用：规模 n=25，对应原例中最大值
    main(25)