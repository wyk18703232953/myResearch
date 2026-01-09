def somaDigitos(x):
    resp = 0
    while x > 0:
        resp += x % 10
        x = x // 10
    return resp

def isReallyBigNumber(x, s):
    return x - somaDigitos(x) >= s

def main(n):
    # 映射规则：
    # 原程序有两个输入：n, s
    # 这里使用参数 n 作为原始 n
    # s 由 n 确定性生成：s = max(0, n // 2)
    N = n
    s = max(0, N // 2)

    ini = 1
    fim = N
    ans = False

    while ini <= fim:
        meio = (ini + fim) // 2
        if isReallyBigNumber(meio, s):
            ans = meio
            fim = meio - 1

        else:
            ini = meio + 1

    if ans:
        result = N - ans + 1

    else:
        result = 0

    # print(result)
    pass
if __name__ == "__main__":
    main(10_000)