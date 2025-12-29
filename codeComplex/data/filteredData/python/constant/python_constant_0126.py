import random

def main(n: int):
    # 根据规模 n 生成一个测试整数字符串 s
    # 这里设定生成范围为 [-10^n + 1, 10^n - 1]
    if n <= 0:
        n = 1
    lower = -10 ** n + 1
    upper = 10 ** n - 1
    x = random.randint(lower, upper)
    s = str(x)

    if int(s) < 0:
        k = int(s) // 10  # 使用整除，匹配原逻辑应对负数的结果
        m = s[:len(s) - 2] + s[-1]
        result = max(int(k), int(m))
    else:
        result = int(s)

    print(result)


if __name__ == "__main__":
    # 示例调用：规模 n = 3
    main(3)