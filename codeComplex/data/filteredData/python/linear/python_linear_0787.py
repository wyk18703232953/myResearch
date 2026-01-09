from collections import Counter


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
    # n 表示数组长度
    # 构造一个确定性的非降数组，类似原题中的 A
    # 示例构造：A[i] = i // 2，使得有一些重复元素但规模随 n 线性增长
    A = [i // 2 for i in range(n)]
    # 调用原逻辑
    if check(A):
        # print('sjfnb')
        pass

    else:
        # print('cslnb')
        pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小做规模实验
    main(10)