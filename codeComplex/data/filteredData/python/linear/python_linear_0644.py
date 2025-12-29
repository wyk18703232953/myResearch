import random

def main(n):
    # 生成测试数据 a：长度为 n 的正整数元组
    # 这里示例生成 1~3 的随机整数，可按需要调整生成规则
    a = tuple(random.randint(1, 3) for _ in range(n))

    if n * 2 > sum(a) + 2:
        print("NO")
    else:
        n1 = []
        on = []
        for i in range(n):
            if a[i] != 1:
                n1.append(i)
            else:
                on.append(i)
        print("YES", len(n1) + min(2, len(on)) - 1)
        print(n - 1)
        n1it = iter(n1)
        next(n1it)
        for v, u in zip(n1, n1it):
            print(v + 1, u + 1)
        if on:
            print(on.pop() + 1, n1[-1] + 1)
        if on:
            print(on.pop() + 1, n1[0] + 1)
        on_iter = iter(on)
        for n11 in n1:
            for _ in range(a[n11] - 2):
                try:
                    print(n11 + 1, next(on_iter) + 1)
                except StopIteration:
                    break
            else:
                continue
            break


if __name__ == "__main__":
    # 示例运行：n = 5，可按需要修改或在其他模块中调用 main(n)
    main(5)