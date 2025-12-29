import random

def digit(a: int) -> int:
    s = 0
    while a:
        s += a % 10
        a //= 10
    return s

def big(n: int, s: int) -> int:
    lo = 1
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid - digit(mid) < s:
            lo = mid + 1
        else:
            hi = mid - 1
    return n - lo + 1

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 1 <= a <= n
    # 1 <= b <= a
    a = random.randint(1, n)
    b = random.randint(1, a)
    # 输出 big(a, b) 的结果
    print(big(a, b))

if __name__ == "__main__":
    # 示例：使用 n = 10**6 作为规模
    main(10**6)