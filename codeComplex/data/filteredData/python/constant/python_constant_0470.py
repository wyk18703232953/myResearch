import random

def main(n):
    # 生成测试数据：棋盘规模 n，随机生成 queen、king、target 的坐标 (0..n-1)
    # 保证三者互不相同
    def rand_pos(exclude=None):
        if exclude is None:
            exclude = set()
        while True:
            p = (random.randint(0, n - 1), random.randint(0, n - 1))
            if p not in exclude:
                return p

    used = set()
    queen = rand_pos(used)
    used.add(queen)
    king = rand_pos(used)
    used.add(king)
    target = rand_pos(used)

    # 原逻辑
    def done():
        print("NO")

    def complete():
        print("YES")

    # king is left of queen
    if king[0] < queen[0]:
        if target[0] > queen[0]:
            done()
            return
        # king is higher than queen
        if king[1] > queen[1]:
            if target[1] < queen[1]:
                done()
                return
            complete()
            return
        else:
            if target[1] > queen[1]:
                done()
                return
            complete()
            return
    else:
        if target[0] < queen[0]:
            done()
            return
        if king[1] > queen[1]:
            if target[1] < queen[1]:
                done()
                return
            complete()
            return
        else:
            if target[1] > queen[1]:
                done()
                return
            complete()
            return

# 示例调用
if __name__ == "__main__":
    # 可按需修改 n 的规模
    main(8)