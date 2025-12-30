import random

def solve(a):
    n = len(a)
    if n == 0:
        return -1, -1
    m = len(a[0]) if a[0] else 0

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
    right = 10**9 + 1
    i, j = 0, 0
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
    # 生成规模为 n 的测试数据
    # 假设列数 m 与 n 同阶，例如 m = min(n, 20) 以控制位运算规模
    m = min(n, 20)
    # 随机生成 [0, 1e9] 范围内的整数矩阵
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    i, j = solve(a)
    print(i, j)


if __name__ == "__main__":
    # 示例调用：可以修改为任意所需规模
    main(5)