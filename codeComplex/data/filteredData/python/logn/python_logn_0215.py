import random

def somaDigitos(x: int) -> int:
    resp = 0
    while x > 0:
        resp += x % 10
        x //= 10
    return resp

def count_really_big_numbers(n: int, s: int) -> int:
    def isReallyBigNumber(x: int) -> bool:
        return x - somaDigitos(x) >= s

    ini = 1
    fim = n
    ans = None

    # Busca binária para achar o menor x em [1, n] tal que x - somaDigitos(x) >= s
    while ini <= fim:
        meio = (ini + fim) // 2
        if isReallyBigNumber(meio):
            ans = meio
            fim = meio - 1
        else:
            ini = meio + 1

    if ans is not None:
        return n - ans + 1
    else:
        return 0

def main(n: int):
    # 根据 n 生成测试数据，这里令 s 为 [0, n] 范围内的随机整数
    # 若需要确定性测试，可将 s 固定为某个函数，例如 s = n // 2
    random.seed(0)
    s = random.randint(0, n) if n > 0 else 0

    result = count_really_big_numbers(n, s)
    print(result)

# 示例：如需直接运行，可取消下面注释
# if __name__ == "__main__":
#     main(10)