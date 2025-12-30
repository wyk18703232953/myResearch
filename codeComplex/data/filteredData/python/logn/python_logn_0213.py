def really_big(ni, s):
    dig_sum = sum(map(int, str(ni)))
    return (ni - dig_sum) >= s

def main(n):
    # 根据 n 生成测试数据，这里约定 s = n // 2 作为示例规模关系
    s = n // 2

    cont = 0
    for i in range(s, n + 1):
        if really_big(i, s):
            cont = n - i + 1
            break

    print(cont)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)