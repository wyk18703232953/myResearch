from itertools import accumulate
from random import randint


def Binary_Search(arr, x, n):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1


def main(n):
    # 生成测试数据
    # 怪物血量数组 a（长度 n，正整数）
    a = [randint(1, 10) for _ in range(n)]
    # 查询次数 q
    q = n
    # 每次攻击的伤害数组 b（长度 q，正整数）
    b = [randint(1, 10) for _ in range(q)]

    ps = list(accumulate(a))
    ans = []

    arrows = 0
    for arrow in b:
        arrows += arrow
        if arrows >= ps[-1]:
            ans.append(n)
            arrows = 0
        else:
            res = Binary_Search(ps, arrows, n)
            ans.append(n - res)

    for x in ans:
        print(x)


if __name__ == "__main__":
    # 示例调用：规模 n 可自行修改
    main(5)