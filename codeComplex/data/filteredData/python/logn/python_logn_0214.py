def somadig(x: int) -> int:
    soma = 0
    while x > 0:
        soma += x % 10
        x //= 10
    return soma


def solve(x: int, s: int) -> int:
    comeco = 9
    fim = x
    if comeco >= fim:
        return 0

    while fim >= comeco:
        meio = (fim + comeco) // 2
        if meio - somadig(meio) >= s:
            if (meio - 1) - somadig(meio - 1) < s:
                return x - (meio - 1)
            fim = meio - 1
        else:
            comeco = meio + 1

    return 0


def main(n: int):
    """
    按规模 n 生成测试数据并执行原逻辑。
    这里将：
      x = n
      s = n // 2
    你可以按需要修改生成规则。
    """
    x = n
    s = n // 2
    ans = solve(x, s)
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 100
    main(100)