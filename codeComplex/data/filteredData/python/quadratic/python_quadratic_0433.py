def solve(x, arr):
    n = len(arr)
    flag = True
    k = []
    i = 0
    while flag:
        sm = 0
        while n > 0 and sm < x:
            sm += int(arr[i])
            i += 1
            n -= 1
            if n <= 0:
                flag = False
                break
        if sm > 0:
            k.append(sm)
    return k


def main(n):
    # 生成长度为 n 的只含 '0' 和 '1' 的测试数据
    # 简单策略：周期性重复 "01"
    s = [(i % 2) for i in range(n)]  # 数值数组，稍后转成字符

    # 保留原逻辑：s 最终要是字符列表
    s_chars = [str(x) for x in s]

    if len(set(s_chars)) == 1:
        # print('YES')
        pass
        return

    l = []
    t = 0
    for i in range(n - 1):
        t += int(s_chars[i])
        l.append(t)

    for i in l:
        if i > 0:
            r = solve(i, s_chars)
            if len(r) > 1 and len(set(r)) == 1:
                # print('YES')
                pass
                break

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例运行：可根据需要修改规模
    main(10)