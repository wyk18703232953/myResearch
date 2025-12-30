import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 约定：n 表示数值位数上限（大致 2^n 的数量级）
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)  # 保证 l <= r

    # 以下为原逻辑的封装，无 input()
    if l == r:
        ans = 0
    else:
        rr = r
        rs = ""
        while rr:
            rs += '1' if rr % 2 else '0'
            rr //= 2
        for _ in range(len(rs), 65):
            rs += '0'

        ll = l
        ls = ""
        while ll:
            ls += '1' if ll % 2 else '0'
            ll //= 2
        for _ in range(len(ls), 65):
            ls += '0'

        pos = -1
        for i in range(64, -1, -1):
            if rs[i] == '1' and ls[i] == '0':
                pos = i
                break

        ans = 2 ** (pos + 1) - 1

    print(ans)


if __name__ == '__main__':
    # 示例：规模为 10，可根据需要修改
    main(10)