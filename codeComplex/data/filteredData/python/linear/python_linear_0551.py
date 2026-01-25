from math import *

def main(n):
    # 生成确定性输入数据：长度为 n 的整数列表
    A = [i // 2 for i in range(n)]

    ans = -1
    maxs = 0
    for j in range(n):
        if A[j] > maxs:
            ans = j + 1
            break
        else:
            maxs = max(maxs, A[j] + 1)
    print(ans)


if __name__ == "__main__":
    main(10)