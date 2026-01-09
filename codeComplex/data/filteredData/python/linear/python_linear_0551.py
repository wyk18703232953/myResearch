from math import *

def main(n):
    # 确定性生成长度为 n 的数组 A
    # 这里构造一个模式：前半部分不满足条件，后半部分逐渐增大
    A = [(i // 2) for i in range(n)]

    ans = -1
    maxs = 0
    for j in range(n):
        if A[j] > maxs:
            ans = j + 1
            break

        else:
            maxs = max(maxs, A[j] + 1)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)