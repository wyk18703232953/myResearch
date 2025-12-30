import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 将棋盘视为 n x n，随机生成皇后(Q)、国王(K)以及第三个点(C)的坐标
    # 坐标范围为 [1, n]
    ax, ay = random.randint(1, n), random.randint(1, n)  # 皇后位置
    bx, by = random.randint(1, n), random.randint(1, n)  # 国王位置
    cx, cy = random.randint(1, n), random.randint(1, n)  # 第三个点

    # 输出生成的测试数据（如不需要，可移除此部分）
    print(f"n = {n}")
    print(f"Queen (ax, ay) = ({ax}, {ay})")
    print(f"King  (bx, by) = ({bx}, {by})")
    print(f"Point (cx, cy) = ({cx}, {cy})")

    # 原始逻辑
    if bx < ax < cx or bx > ax > cx or by < ay < cy or cy < ay < by:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(10)