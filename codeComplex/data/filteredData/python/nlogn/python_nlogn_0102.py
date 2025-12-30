import random

def main(n):
    # 随机生成 nab 数组：[n, ?, k]
    # 为了保证索引合法，令 k 在 [1, n-1] 之间
    if n < 2:
        # 不足以产生有效对比，直接返回
        return

    k = random.randint(1, n - 1)
    nab = [n, 0, k]  # 第二个元素在原逻辑中未使用，可任意

    # 生成长度为 n 的随机整数数组 l
    # 数值范围可按需调整
    l = [random.randint(0, 1000) for _ in range(n)]

    l.sort()

    # 对应原逻辑：比较 l[k-1] 和 l[k]
    if l[nab[2] - 1] == l[nab[2]]:
        print(0)
    else:
        print(l[nab[2]] - l[nab[2] - 1])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)