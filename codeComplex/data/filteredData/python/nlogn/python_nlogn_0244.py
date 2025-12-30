import random

def binarySearch_LowerBound(arr, key):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] > key:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1


def Solution(N, Q, wariors_strength, arrows):
    prefix_sum = [0]
    for strength in wariors_strength:
        prefix_sum.append(prefix_sum[-1] + strength)
    prefix_sum.pop(0)

    arrow_so_far = 0
    for arrow in arrows:
        arrow_so_far += arrow
        if arrow_so_far >= prefix_sum[-1]:
            print(N)
            arrow_so_far = 0
        else:
            idx = binarySearch_LowerBound(prefix_sum, arrow_so_far)
            print(N - idx)


def main(n):
    # n 作为规模，用来生成 N、Q 以及对应大小的数据
    # 这里简单设定：N = n, Q = n
    N = n
    Q = n

    # 生成测试数据：
    # 战士战斗力：1 到 10 之间的随机整数
    wariors_strength = [random.randint(1, 10) for _ in range(N)]

    # 箭的威力：1 到 10 之间的随机整数
    arrows = [random.randint(1, 10) for _ in range(Q)]

    Solution(N, Q, wariors_strength, arrows)


# 示例：当作为脚本运行时，用某个规模调用 main
if __name__ == "__main__":
    main(10)