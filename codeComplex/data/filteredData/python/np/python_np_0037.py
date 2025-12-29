import random

def factorial(n: int) -> int:
    total = 1
    for i in range(n):
        total *= (i + 1)
    return total

def solve(s1: str, s2: str) -> float:
    objetivo = s1.count("+") - s1.count("-")
    inicio = s2.count("+") - s2.count("-")
    incognitos = s2.count("?")
    distancia = objetivo - inicio

    if abs(distancia) > incognitos or distancia % 2 != incognitos % 2:
        return 0.0
    else:
        mas = (distancia + incognitos) // 2
        menos = (incognitos - distancia) // 2
        return (factorial(incognitos) / (factorial(mas) * factorial(menos))) / (2 ** incognitos)

def main(n: int):
    # 生成测试数据：
    # s1: 长度为 n，由'+'和'-'随机组成
    # s2: 长度为 n，由'+', '-', '?'随机组成
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(choices_s1) for _ in range(n))
    s2 = ''.join(random.choice(choices_s2) for _ in range(n))

    ans = solve(s1, s2)
    print(ans)

if __name__ == "__main__":
    # 示例：规模 n = 10，可根据需要修改
    main(10)