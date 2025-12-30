def NOD(a, b):
    while b != 0:
        a %= b
        a, b = b, a
    return a

def NOK(a, b):
    return (a * b) // NOD(a, b)

def main(n: int):
    # 这里根据 n “生成测试数据”的含义是：
    # 使用给定的 n 作为规模，在区间 [max(1, n-40), n] 内搜索
    maxnok = 0
    x = 40
    delit = []

    for i in range(max(1, n - x), n + 1):
        for j in range(max(1, i - x), i + 1):
            for f in range(max(1, j - x), j + 1):
                nokk = NOK(NOK(i, j), f)
                if maxnok < nokk:
                    maxnok = nokk
                    delit = [i, j, f]

    print(maxnok)

if __name__ == "__main__":
    # 示例：调用 main(100) 进行测试，可根据需要修改 n 的值
    main(100)