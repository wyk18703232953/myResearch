sp = 10**9 + 7

def power(number, n):
    res = 1
    while n != 0:
        if n % 2 != 0:
            res *= number
            res %= sp
            n -= 1
        number *= number
        number %= sp
        n //= 2
    return res % sp

def main(n):
    # 根据规模 n 生成测试数据：
    # 示例：令 x = n, k = n（可按需要修改为其他规则）
    x = n
    k = n

    if x == 0:
        print(0)
    else:
        ans = (
            (((x % sp) * power(2, k)) % sp * 2) % sp
            - (power(2, k) - 1) % sp
        ) % sp
        print(ans)

if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)