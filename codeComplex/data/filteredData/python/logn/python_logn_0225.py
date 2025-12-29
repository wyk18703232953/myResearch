import random

def sum_of_digits(x: int) -> int:
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里令搜索上界为 n，本身即为原程序中的 n
    # s 随机生成在 [0, n] 范围内（也可根据需要调整生成策略）
    s = random.randint(0, n)

    lo, hi = 0, n
    x = n + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid - sum_of_digits(mid) >= s:
            x = min(x, mid)
            hi = mid - 1
        else:
            lo = mid + 1
    result = n - x + 1
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模为 10^6
    main(10**6)