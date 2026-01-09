def main(n):
    # 将 n 映射为 (a, b)：保证 a, b 为正整数且 b != 0
    # 这里使用简单确定性构造
    a = n + 1
    b = (n % 10) + 1

    ans = 0
    if a > b:
        ans += a // b
        a = a % b
    while b != 0:
        ans += a // b
        a, b = b, a % b
    return ans

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行规模实验
    n = 10
    # print(main(n))
    pass