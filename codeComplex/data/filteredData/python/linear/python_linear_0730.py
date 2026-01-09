def main(n):
    # 确定性生成 k，保证 1 <= k <= n
    if n <= 1:
        k = 1

    else:
        k = (n // 2) or 1

    strr = ""
    block_len = (n - k) // 2
    if block_len < 0:
        block_len = 0
    block = "0" * block_len + "1"
    if block == "":
        block = "1"

    while len(strr) < n:
        strr += block
    strr = strr[:n]
    # print(strr)
    pass
if __name__ == "__main__":
    main(10)