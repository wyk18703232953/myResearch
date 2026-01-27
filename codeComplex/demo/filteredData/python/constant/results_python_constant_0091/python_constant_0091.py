import math

def check(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n & 1:
        return (n - 1) * (n - 2) * n
    if math.gcd(n, n - 3) == 1:
        return n * (n - 1) * (n - 3)

    else:
        return (n - 1) * (n - 2) * (n - 3)

def main(n):
    # 使用 n 作为输入规模，并直接作为原算法的输入
    result = check(n)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要更改 n 的值做实验
    main(10)