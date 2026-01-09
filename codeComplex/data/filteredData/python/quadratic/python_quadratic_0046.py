def main(n: int) -> int:
    m = 10**9 + 7

    # 生成测试数据：第一行是 n，后面 n-1 行是 'f' 或 's'
    # 这里简单生成一个模式，比如前一半为 'f'，后一半为 's'
    lines = [str(n) + '\n']
    for i in range(1, n):
        if i <= (n - 1) // 2:
            lines.append('f\n')

        else:
            lines.append('s\n')

    # 以下是原逻辑，只是把 input 替换为 lines
    curr = [0] * (n + 20)
    last = [0] * (n + 20)
    curr[0] = 1

    for s_idx in range(1, n):
        last, curr = curr, last
        if lines[s_idx] == 'f\n':
            curr[0] = 0
            for i in range(len(last) - 1):
                curr[i + 1] = last[i]
        elif lines[s_idx] == 's\n':
            curr[-1] = 0
            for i in range(len(last) - 2, -1, -1):
                curr[i] = (curr[i + 1] + last[i]) % m

    s = 0
    for x in curr:
        s = (s + x) % m
    return s


if __name__ == "__main__":
    # 示例：调用 main(5) 并打印结果
    # print(main(5))
    pass