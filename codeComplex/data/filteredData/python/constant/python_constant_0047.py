import math
import random

def islucky(x):
    digits = set(str(x))
    return ((len(digits) == 2 and "4" in digits and "7" in digits) or
            (len(digits) == 1 and ("4" in digits or "7" in digits)))

def main(n):
    # 根据规模 n 生成测试数据：生成一个 1 到 10^n 之间的随机整数
    if n <= 0:
        a = 1
    else:
        upper = 10 ** n - 1
        a = random.randint(1, upper)

    lucky = islucky(a)
    for i in range(2, math.isqrt(a) + 1):
        if a % i == 0:
            if islucky(i) or islucky(a // i):
                lucky = True
                break

    print("YES" if lucky else "NO")

if __name__ == "__main__":
    # 示例：使用 n=3 运行
    main(3)