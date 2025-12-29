import math
import random

def main(n):
    # 生成测试数据：长度为 n 的随机正整数列表
    # 这里生成 1~10 之间的随机整数，可根据需要调整范围
    lst = [random.randint(1, 10) for _ in range(n)]

    # 原逻辑开始
    p = max(lst)
    ind = lst.index(p)
    if p == 1:
        lst[ind] = 2
    else:
        lst[ind] = 1

    lst.sort()
    for j in range(n):
        print(lst[j], end=" ")

if __name__ == "__main__":
    # 示例：调用 main(5)，规模 n 可在此修改
    main(5)