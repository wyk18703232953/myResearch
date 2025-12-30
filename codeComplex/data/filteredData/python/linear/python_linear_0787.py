from collections import Counter
import random

def check(A):
    CA = Counter(A)
    if CA[0] >= 2:
        return False
    cnt = 0
    for k, v in CA.items():
        if v > 2:
            return False
        if v == 2 and CA[k - 1] >= 1:
            return False
        if v >= 2:
            cnt += 1
    if cnt >= 2:
        return False
    L = len(A)
    if (sum(A) - L * (L - 1) // 2) % 2 == 0:
        return False
    return True


def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的非负整数数组
    # 这里生成 0 到 2n 范围内的随机整数
    A = [random.randint(0, 2 * n) for _ in range(n)]

    if check(A):
        print('sjfnb')
    else:
        print('cslnb')


if __name__ == "__main__":
    # 示例：可在此处指定规模 n 进行本地测试
    main(5)