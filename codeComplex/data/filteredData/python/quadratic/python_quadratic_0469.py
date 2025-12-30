import random

def main(n):
    # 生成一组可行的测试数据 (l, r, out)
    # 思路：先随机生成一个 1..n 的排列 out，然后根据算法的反向过程构造 l 和 r
    out = list(range(1, n + 1))
    random.shuffle(out)

    # 反向构造 l, r
    # 原算法是从 a = n..1 依次确定 out 中的值，
    # 我们倒着模拟它，得到合法的 l, r
    l = [0] * n
    r = [0] * n
    # 逆向状态：我们从 a = 1..n 依次“插入”元素
    # 使用和原算法对应的 mp 映射，但这里逆向构造时 mp 始终是 i->i
    # 因为我们直接在最终位置上推 l, r 约束
    # 推导：当 out[p] = a 确定时，对所有 j:
    # j < p: r[j] += 1
    # j >= p: l[j] += 1
    for a in range(1, n + 1):
        p = out.index(a)
        for j in range(n):
            if j < p:
                r[j] += 1
            else:
                l[j] += 1

    # 现在用给出的算法跑一遍，验证并输出
    mp = {i: i for i in range(n)}
    out_calc = [-1] * n
    v = 0

    a = n
    done = set()
    while v < n:
        ids = set()
        for j in range(n):
            if l[j] == r[j] == 0 and j not in done:
                ids.add(j)
                done.add(j)
        if len(ids) == 0:
            print('NO')
            return
        v += len(ids)
        for i in ids:
            out_calc[mp[i]] = a
            for j in range(len(l)):
                if j < i:
                    r[j] -= 1
                else:
                    l[j] -= 1
        a -= 1
    print('YES')
    print(' '.join(map(str, out_calc)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)