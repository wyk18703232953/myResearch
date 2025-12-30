def inn(a, b):
    return (a[0] <= b[0] and b[1] <= a[1])

def generate_segments(n):
    # 生成 n 个线段 (l, r)，保证 l < r
    # 简单策略：第 i 个线段为 (i, i*2)
    segs = []
    for i in range(1, n + 1):
        l = i
        r = i * 2
        segs.append((l, r, i))
    return segs

def main(n):
    seg = generate_segments(n)

    seg.sort(key=lambda x: (x[0], -x[1]))

    main_seg = seg.pop(0)

    for s in seg:
        if inn(main_seg, s):
            print(s[2], main_seg[2])
            return
        if main_seg[1] < s[1]:
            main_seg = s

    print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改
    main(5)