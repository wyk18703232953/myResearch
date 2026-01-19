def main(n):
    # 根据 n 生成 6 个边长参数 a,b,c,d,e,f
    # 完全确定性：使用简单算术构造
    a = n
    b = n + 1
    c = n + 2
    d = n + 3
    e = n + 4
    f = n + 5

    a, b, c, d, e, f = int(a), int(b), int(c), int(d), int(e), int(f)

    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if e < f:
        e, f = f, e

    sides = [[a, b, "A"], [c, d, "B"], [e, f, "C"]]
    sides.sort(reverse=True)
    c1, c2, c3 = sides[0][2], sides[1][2], sides[2][2]

    area = a * b + c * d + e * f
    if int(area ** 0.5) ** 2 != area:
        print(-1)
        return
    else:
        l = int(area ** 0.5)
        if l not in sides[0]:
            print(-1)
            return
        elif l in sides[1] and l in sides[2]:
            print(l)
            for i in range(3):
                sides[i].remove(l)
            for i in range(3):
                for _ in range(sides[i][0]):
                    print([c1, c2, c3][i] * l)
        else:
            r = l - sides[0][1]
            if r in sides[1] and r in sides[2]:
                print(l)
                for i in range(1, 3):
                    sides[i].remove(r)
                for _ in range(sides[0][1]):
                    print(c1 * l)
                for _ in range(r):
                    print(c2 * sides[1][0] + c3 * sides[2][0])
            else:
                print(-1)


if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(5)