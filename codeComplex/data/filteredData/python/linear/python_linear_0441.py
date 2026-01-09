ceil1 = lambda a, b: (a + b - 1) // b

def main(n: int):
    # 根据 n 生成测试数据（此处测试数据就是 n 自身）
    sq = int(n ** 0.5)
    sq2, ans, cur = ceil1(n, sq), [], 0

    for _ in range(sq2 - 1):
        cur += sq
        ans.extend([x for x in range(cur, cur - sq, -1)])

    ans.extend([x for x in range(n, cur, -1)])
    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(10)