import sys
import io

def main(n):
    # 将输入规模 n 映射为:
    #   n_points = n         点的数量
    #   a, b 由 n 确定性构造
    if n < 1:
        print(0)
        return

    n_points = n
    a = n % 7 + 1   # a ∈ [1,7]
    b = n % 11 + 1  # b ∈ [1,11]

    dc = {}
    for i in range(n_points):
        # 确定性生成 x, vx, vy
        x = i
        vx = (i * 2 + 3) % (2 * n_points + 5) - n_points  # 有正有负
        vy = (i * 3 + 5) % (2 * n_points + 7) - n_points

        nx = x + vx
        ny = a * x + b + vy
        dd = a * nx - ny + b

        if dd not in dc:
            dc[dd] = {}
        key = (vx, vy)
        if key not in dc[dd]:
            dc[dd][key] = 0
        dc[dd][key] += 1

    tot = 0
    for _, k in dc.items():
        tt = 0
        pp = 0
        for _, cc in k.items():
            tt -= cc * (cc + 1) // 2
            pp += cc
        tt += pp * (pp + 1) // 2
        tot += tt * 2

    print(tot)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小
    main(10)