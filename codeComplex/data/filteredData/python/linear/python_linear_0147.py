def main(n):
    # 确定性生成输入数据
    p = n + 7 if n > 0 else 7
    a = [(i * 3 + 1) % p for i in range(n)] if n > 0 else [0]

    # 保持原算法逻辑
    forward = [a[0]]
    for i in range(1, n):
        forward.append(forward[-1] + a[i])
    sm = sum(a)
    mx = -float('inf')
    for i in range(n - 1):
        mx = max(mx, (forward[i] % p) + ((sm - forward[i]) % p))
    # print(mx)
    pass
if __name__ == "__main__":
    main(10)