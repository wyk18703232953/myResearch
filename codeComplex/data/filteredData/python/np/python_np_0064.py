from math import factorial as fact
import random

def solve(s1: str, s2: str) -> float:
    plus1 = s1.count("+")
    minus1 = s1.count("-")

    plus2 = s2.count("+")
    minus2 = s2.count("-")
    qCount = s2.count("?")

    if plus1 == plus2 and minus1 == minus2:
        return 1.0
    else:
        plusReq = plus1 - plus2
        minusReq = minus1 - minus2
        if plusReq >= 0 and minusReq >= 0 and plusReq + minusReq == qCount:
            ans = (0.5 ** qCount) * fact(qCount) / (fact(plusReq) * fact(minusReq))
            return ans
        else:
            return 0.0

def generate_test_data(n: int):
    # n 为第一行目标字符串 s1 的长度
    # 第二行 s2 按相同长度生成，字符来自 '+', '-', '?'
    s1 = "".join(random.choice(["+", "-"]) for _ in range(n))
    s2 = "".join(random.choice(["+", "-", "?"]) for _ in range(n))
    return s1, s2

def main(n: int):
    s1, s2 = generate_test_data(n)
    ans = solve(s1, s2)
    print(ans)

if __name__ == "__main__":
    # 示例执行，可根据需要修改 n
    main(5)