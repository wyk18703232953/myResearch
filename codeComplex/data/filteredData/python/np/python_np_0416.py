import random


def solve(a):
    n = len(a)
    m = len(a[0]) if n > 0 else 0

    def check(mid):
        mask = (1 << m) - 1
        s = set()
        d = dict()
        for i in range(n):
            state = 0
            for j in range(m):
                if a[i][j] >= mid:
                    state |= 1 << j
            if state in s:
                continue
            s.add(state)
            k = state
            while k >= 0:
                k &= state
                d[k] = i
                k -= 1
            need = mask ^ state
            if need in d:
                q1, q2 = d[need], i
                if q1 > q2:
                    q1, q2 = q2, q1
                return True, (q1, q2)
        return False, (-1, -1)

    left = 0
    right = 10 ** 9 + 1
    i = j = 0
    while right - left > 1:
        mid = (right + left) // 2
        flag, (q1, q2) = check(mid)
        if flag:
            left = mid
            i, j = q1, q2
        else:
            right = mid
    return i + 1, j + 1


def main(n):
    # 生成测试数据：
    # n 行，m 列；元素为 [0, 1e9] 区间内的随机整数
    m = max(1, min(10, n))  # 简单设定列数，避免过大
    a = [[random.randint(0, 10 ** 9) for _ in range(m)] for _ in range(n)]

    i, j = solve(a)
    print(i, j)


if __name__ == "__main__":
    # 示例规模，可在外部修改调用 main(n)
    main(5)