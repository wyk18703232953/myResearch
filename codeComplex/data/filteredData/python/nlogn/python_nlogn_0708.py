import random

def main(n: int):
    # 1. 生成测试数据：n个非负整数
    # 为了贴近原问题场景（通常是类似 Nim 的博弈），生成较小的非负整数
    a = [random.randint(0, n) for _ in range(n)]

    a = sorted(a)

    win = None
    first = True

    if n == 1:
        win = a[0] % 2 == 1
    elif a[1] == 0:
        win = False

    if n > 2:
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                if i > 0:
                    if a[i - 1] == a[i] - 1:
                        win = False
                        break
                if not first:
                    win = False
                    break
                first = False

    if win is None:
        win = (sum(a) - (n * (n - 1) // 2)) % 2 == 1

    if win:
        print('sjfnb')
    else:
        print('cslnb')


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)