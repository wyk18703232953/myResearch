def fis(sq):
    if sq[2] < sq[0] or sq[3] < sq[1]:
        return [0, 0]
    sc = (sq[0] + sq[1]) % 2
    fc = (sq[2] + sq[3]) % 2
    sxl = sq[2] - sq[0] + 1
    syl = sq[3] - sq[1] + 1
    hf = (sxl * syl) // 2
    cp = -1
    if sc == fc and (sxl + syl) % 2 == 0 and sxl % 2 == 1:
        cp = sc
    return [hf + (1 if cp == 0 else 0), hf + (1 if cp == 1 else 0)]


def main(n):
    """
    n: 规模参数，用于生成 n 组测试数据
    这里生成的测试数据策略（可按需要修改）：
    - 对于第 i 组：
        m = 10 + i     # 棋盘宽
        k = 10 + 2*i   # 棋盘高（对应原代码中的 n，但避免变量名冲突）
        wco: 左上 1,1，右下为 (m//2, k//2)
        bco: 左上为 (m//3, k//3)，右下为 (m, k)
    """
    import random

    results = []
    for i in range(n):
        m = 10 + i          # 原代码中的 m（列数）
        k = 10 + 2 * i      # 原代码中的 n（行数）

        # 生成白色区域 wco: [x1, y1, x2, y2]
        w_x1, w_y1 = 1, 1
        w_x2, w_y2 = max(1, m // 2), max(1, k // 2)
        wco = [w_x1, w_y1, w_x2, w_y2]

        # 生成黑色区域 bco，确保在棋盘内
        b_x1 = max(1, m // 3)
        b_y1 = max(1, k // 3)
        b_x2 = m
        b_y2 = k
        bco = [b_x1, b_y1, b_x2, b_y2]

        # 原逻辑
        wf, bf = fis([1, 1, m, k])
        btw = fis(wco)[1]
        wtb = fis(bco)[0]
        bnac = [
            max(wco[0], bco[0]),
            max(wco[1], bco[1]),
            min(wco[2], bco[2]),
            min(wco[3], bco[3]),
        ]
        bna = fis(bnac)[1]
        white = wf + btw - wtb - bna
        black = bf + wtb - btw + bna

        results.append((white, black))

    # 输出所有结果
    for w, b in results:
        print(w, b)


if __name__ == "__main__":
    # 示例：运行 3 组自动生成的数据
    main(3)