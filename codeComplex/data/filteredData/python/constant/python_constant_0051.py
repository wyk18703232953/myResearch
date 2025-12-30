import math
import random

def lucky(x: int) -> bool:
    s = set(str(x))
    return s.issubset({"4", "7"}) and len(s) > 0

def main(n: int):
    # 根据规模 n 生成一个测试数 a
    # 这里简单设定：在 [1, 10^n] 范围内随机生成
    if n <= 0:
        a = 1
    else:
        upper = 10 ** n
        a = random.randint(1, upper)

    is_lucky_divisible = False
    limit = math.isqrt(a)
    for i in range(1, limit + 1):
        if a % i == 0:
            if lucky(i) or lucky(a // i):
                is_lucky_divisible = True
                break

    print("YES" if is_lucky_divisible else "NO")

if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改 n
    main(3)