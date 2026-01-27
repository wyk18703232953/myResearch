def interact_factory(a, b):
    def interact(c, d):
        return max(min((a ^ c) - (b ^ d), 1), -1)
    return interact

def solve_with_interactor(interact):
    def ask(c, d):
        return interact(c, d)

    relative = ask(0, 0)
    curA = 0
    curB = 0

    for i in range(29, -1, -1):
        q1 = ask(curA ^ (1 << i), curB)
        q2 = ask(curA, curB ^ (1 << i))

        if q1 == q2:
            if relative == 1:
                curA ^= (1 << i)

            else:
                curB ^= (1 << i)
            relative = q1
        elif q2 == 1:
            curA ^= (1 << i)
            curB ^= (1 << i)
    return curA, curB

def main(n):
    # 将 n 映射为 a, b 的规模：这里简单设定 a = n, b = n // 2
    a = n
    b = n // 2
    interact = interact_factory(a, b)
    curA, curB = solve_with_interactor(interact)
    # 为了防止优化时被认为无用，返回结果
    return curA, curB

if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    result = main(10**5)
    # print(result)
    pass