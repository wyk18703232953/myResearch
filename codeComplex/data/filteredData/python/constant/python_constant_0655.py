import random

def main(n):
    # 1. 生成规模为 n 的测试数据（n 组测试，每组 3 个点）
    #    这里将坐标范围设置为 [-n, n]，可以按需要调整
    test_cases = []
    for _ in range(n):
        case = []
        for _ in range(3):
            x = random.randint(-n, n)
            y = random.randint(-n, n)
            case.append((x, y))
        test_cases.append(case)

    # 2. 对每一组测试数据执行原逻辑
    out_lines = []
    for a in test_cases:
        a.sort()

        up1 = a[1][1] >= a[0][1]
        up2 = a[2][1] >= a[0][1]
        ans = {a[0]}
        x, y = a[0]

        if up1 and up2:
            while y < min(a[1][1], a[2][1]):
                y += 1
                ans.add((x, y))
            while x < a[2][0]:
                x += 1
                ans.add((x, y))
            hx, hy = a[2] if a[2][1] > a[1][1] else a[1]
            while hy > y:
                ans.add((hx, hy))
                hy -= 1
        else:
            dn1 = a[1][1] <= a[0][1]
            dn2 = a[2][1] <= a[0][1]
            ans = {a[0]}
            x, y = a[0]
            if dn1 and dn2:
                while y > max(a[1][1], a[2][1]):
                    y -= 1
                    ans.add((x, y))
                while x < a[2][0]:
                    x += 1
                    ans.add((x, y))
                lx, ly = a[2] if a[2][1] < a[1][1] else a[1]
                while ly < y:
                    ans.add((lx, ly))
                    ly += 1
            else:
                x, y = a[0]
                ans = {a[0]}
                while x < a[2][0]:
                    x += 1
                    ans.add((x, y))
                dy = 1 if a[1][1] <= a[0][1] else -1
                xx, yy = a[1]
                while yy != a[0][1]:
                    ans.add((xx, yy))
                    yy += dy
                dy = 1 if a[2][1] <= a[0][1] else -1
                xx, yy = a[2]
                while yy != a[0][1]:
                    ans.add((xx, yy))
                    yy += dy

        ans = sorted(ans)
        out_lines.append(str(len(ans)))
        out_lines.extend(f"{x} {y}" for x, y in ans)

    print("\n".join(out_lines))


if __name__ == "__main__":
    # 示例：规模设为 1，表示生成 1 组随机的 3 点测试
    main(1)