import random

def main(n):
    # 根据 n 生成一个测试整数：
    # 这里约定：当 n > 0 时，生成 [-10^n + 1, 10^n - 1] 范围内的随机整数
    # 若需固定测试值，也可直接设 test_value = n 或其他规则
    if n <= 0:
        test_value = 0
    else:
        low = -10**n + 1
        high = 10**n - 1
        test_value = random.randint(low, high)

    # 原始逻辑开始
    x = test_value
    l = list(str(x))
    if x >= 0:
        print(x)
    else:
        if int(l[-1]) > int(l[-2]):
            l.pop(-1)
        else:
            l.pop(-2)
        print(int(''.join(l)))

if __name__ == "__main__":
    # 示例：调用 main(3) 测试 n=3 的情况
    main(3)