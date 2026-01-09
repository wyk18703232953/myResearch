def interact(a, b, c, d):
    return max(min((a ^ c) - (b ^ d), 1), -1)

def solve(a, b):
    def ask(c, d):
        return interact(a, b, c, d)

    relative = ask(0, 0)
    curA = 0
    curB = 0

    for i in range(29, -1, -1):
        q1 = ask(curA ^ (1 << i), curB)
        q2 = ask(curA, curB ^ (1 << i))

        if q1 == q2:
            if relative == 1:
                curA ^= 1 << i

            else:
                curB ^= 1 << i
            relative = q1
        elif q2 == 1:
            curA ^= 1 << i
            curB ^= 1 << i
    return curA, curB

def main(n):
    # 生成规模为 n 的确定性测试：n 组 (a, b)
    # 第 k 组为 (k, 2*k)
    res = []
    for k in range(n):
        a = k
        b = 2 * k
        curA, curB = solve(a, b)
        res.append((curA, curB))
    return res

if __name__ == "__main__":
    # 示例调用：n = 5
    ans = main(5)
    for pair in ans:
        # print(pair[0], pair[1])
        pass