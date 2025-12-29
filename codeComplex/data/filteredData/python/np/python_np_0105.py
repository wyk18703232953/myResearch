import math
import random

def find_nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def solve(sent: str, received: str) -> float:
    final_pos = 0
    current_pos = 0
    uncertain = 0

    for s in sent:
        if s == "+":
            final_pos += 1
        else:
            final_pos -= 1

    for s in received:
        if s == "+":
            current_pos += 1
        elif s == "-":
            current_pos -= 1
        else:
            uncertain += 1

    if uncertain == 0:
        return 1.0 if final_pos == current_pos else 0.0
    else:
        positions = list(range(current_pos - uncertain, current_pos + uncertain + 2, 2))
        try:
            pos_index = positions.index(final_pos)
        except ValueError:
            return 0.0
        a = find_nCr(uncertain, pos_index)
        b = math.pow(2, uncertain)
        return a / b

def generate_test_data(n: int):
    # n 表示 sent/received 字符串的长度
    symbols_sent = ["+", "-"]
    symbols_received = ["+", "-", "?"]
    sent = "".join(random.choice(symbols_sent) for _ in range(n))
    received = "".join(random.choice(symbols_received) for _ in range(n))
    return sent, received

def main(n: int):
    sent, received = generate_test_data(n)
    result = solve(sent, received)
    print(result)

if __name__ == "__main__":
    # 示例：用规模 n=10 运行
    main(10)