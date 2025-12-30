import random

def main(n):
    # 1. 生成测试数据
    # 按原程序含义，需要生成 n 和 m 以及长度为 n 的数组 a
    # 这里只构造一个可重复使用的 m，并生成随机数组 a
    m = max(1, n // 2)  # m 在原代码中未参与后续逻辑，仅占位
    
    # 生成数组 a：元素取 0~n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    # 2. 将原逻辑封装到 main 中
    ll = sorted(a)
    mx = ll[n - 1] - 1
    cc = 0

    for i in range(n - 2, -1, -1):
        if ll[i] == 0:
            continue
        if mx == 0:
            cc += ll[i] - 1
            continue

        if ll[i] >= mx:
            cc += 1
            mx -= 1
            cc += ll[i] - 1
            ll[i] = 1
        else:
            mx = ll[i]
            cc += 1
            mx -= 1
            cc += ll[i] - 1
            ll[i] = 1

    print(cc)


if __name__ == "__main__":
    # 示例：调用 main 并指定规模 n
    main(10)