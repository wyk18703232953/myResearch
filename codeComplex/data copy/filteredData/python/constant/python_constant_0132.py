def resistors(a, b):
    ans = 0
    while b:
        ans += a // b
        a, b = b, a % b
    return ans

def main(n):
    if n < 1:
        return
    # 生成确定性的 (a, b)，保证 b != 0
    a = n * 2
    b = n if n % 2 == 1 else n + 1
    result = resistors(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)