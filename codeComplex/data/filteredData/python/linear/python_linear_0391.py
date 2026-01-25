def main(n):
    p = 998244353
    # 生成确定性的输入 a，长度为 n
    # 使用简单规则：a[i] = (i % 10)，确保为整数
    a = [i % 10 for i in range(n)]
    answer = a[-1]
    pow_ = 1
    for i in range(n - 1, 0, -1):
        answer = (answer + a[i - 1] * (2 + n - i) * pow_ % p) % p
        pow_ = pow_ * 2 % p
    return answer


if __name__ == "__main__":
    print(main(10))