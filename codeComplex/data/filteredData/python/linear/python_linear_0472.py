import random

def main(n: int):
    # 1. 生成测试数据
    # 生成费用数组 C：1 到 10^9 的随机整数
    C = [random.randint(1, 10**9) for _ in range(n)]

    # 生成一个包含至少一个环的函数式图 A（每个点出度为 1）
    # 方法：先生成一个随机排列，然后再随机打一些自环/重边，保证有环
    A = list(range(n))
    random.shuffle(A)
    # 随机修改若干位置成自环或指向任意节点，保证多样性
    for i in range(random.randint(0, n)):
        v = random.randint(0, n - 1)
        u = random.randint(0, n - 1)
        A[v] = u

    # 把映射改成 0-based 形式（原题中是读入后减 1，这里本来就是 0-based）

    visit = [False] * n
    loops = []

    for i in range(n):
        if not visit[i]:
            s = [i]
            temp = set()
            temp.add(i)
            flag = False
            while s:
                v = s.pop()
                if visit[A[v]]:
                    break
                if A[v] in temp:
                    flag = True
                    p = A[v]
                    break
                else:
                    s.append(A[v])
                    temp.add(A[v])
            if flag:
                loop = [p]
                nv = A[p]
                while nv != p:
                    loop.append(nv)
                    nv = A[nv]
                loops.append(loop)
            for v in temp:
                visit[v] = True

    ans = 0
    for l in loops:
        m = 10**18
        for i in l:
            m = min(m, C[i])
        ans += m

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)