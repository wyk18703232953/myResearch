import collections


def main():
    # # n = int(input())
    # x, y, z, t1, t2, t3 = list(map(int, input().split()))
    # stair = t1 * abs(y - x)
    # ele = t2 * (abs(y - x) + abs(z - x)) + 3 * t3
    # # print(stair, ele)
    # print("YES" if ele <= stair else "NO")

    # n = int(input())
    # num = list(map(int, input().split()))
    # prevMax, totMax = -1, float('-inf')
    # for i, v in enumerate(num):
    #     totMax = max(totMax, v)
    #     if totMax - prevMax in [0, 1]:
    #         prevMax = totMax
    #     else:
    #         print(i + 1)
    #         return
    # print(-1)

    n = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    res = [0] * n
    val = n

    if all(not left[i] and not right[i] for i in range(n)):
        print("YES")
        print(' '.join(['1'] * n))
        return

    while not all(not left[i] and not right[i] for i in range(n)):
        zeroSet = set()
        for i in range(n):
            if not left[i] and not right[i] and res[i] == 0:
                zeroSet.add(i)
                res[i] = val
        for v in zeroSet:
            for i in range(v + 1, n):
                if i not in zeroSet and res[i] == 0:
                    left[i] -= 1
            for i in range(v):
                if i not in zeroSet and res[i] == 0:
                    right[i] -= 1
        val -= 1
        # print(zeroSet, left, right)
        if not zeroSet:
            print("NO")
            return

    for i in range(n):
        if not res[i]:
            res[i] = str(val)
        else:
            res[i] = str(res[i])
    if any(i == '0' for i in res):
        print("NO")
        return
    print("YES")
    print(' '.join(res))


main()
