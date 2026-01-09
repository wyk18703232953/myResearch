def main(n):
    # 映射 n 到 a, b 的规模
    if n <= 0:
        return 0
    a = n
    b = n // 2 + 1  # 保证 b 不为 0 且与 a 有一定差异
    ans = 0
    while a and b:
        ans += a // b
        a, b = b, a % b
    return ans

if __name__ == "__main__":
    # 示例调用
    for n in range(1, 11):
        # print(n, main(n))
        pass