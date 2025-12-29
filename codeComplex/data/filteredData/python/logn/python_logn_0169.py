import random

def main(n):
    # 随机生成一个可行的 k，使得一定存在解
    # 条件：1 + k*(k-1)//2 >= n
    # 简单做法：从较小范围内随机取 k，直到满足条件
    if n == 1:
        # 原逻辑：n == 1 时答案恒为 0
        print(0)
        return

    # 生成满足 1 + k*(k-1)//2 >= n 的 k
    # 为了控制规模，这里限制 k 不超过 2n
    while True:
        k = random.randint(1, max(1, 2 * n))
        if 1 + (k * (k - 1)) // 2 >= n:
            break

    # 以下为原逻辑去掉 input() 后的实现
    ini, fin = 1, k - 1

    if 1 + (k * (k - 1)) // 2 < n:
        print(-1)
        return

    while ini < fin:
        mid = (ini + fin) // 2
        s = 1 + (k - 1) * mid - (mid * (mid - 1)) // 2
        if s >= n:
            fin = mid
        else:
            ini = mid + 1

    print(ini)

# 示例：直接调用 main(n) 测试
if __name__ == "__main__":
    main(10)