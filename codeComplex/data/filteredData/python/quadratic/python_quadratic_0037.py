def main(n):
    mod = 10 ** 9 + 7

    # 输入结构分析：
    # 原程序：
    #   n = int(input())
    #   然后读入 n 行，每行是 'f' 或其他。
    #
    # 将 n 视作“代码行数规模”，并构造一个确定性的缩进结构：
    # 这里选择：前 n // 2 行为 'f'，后 n - n // 2 行为其他（用 's'）
    # 这样既能产生一定缩进层次，又保证确定性和可规模化。
    arr = ['f' if i < n // 2 else 's' for i in range(n)]

    indent_num = 0
    for i in range(n):
        if arr[i] == 'f':
            indent_num += 1

    dp = [0 for _ in range(indent_num + 1)]
    max_indent = 0
    cur_indent = 0
    pref = [0 for _ in range(indent_num + 1)]

    def cal_pref(dp_list, pref_list):
        pref_list[0] = dp_list[0]
        for i in range(1, len(dp_list)):
            pref_list[i] = pref_list[i - 1] + dp_list[i]

    for i in range(n):
        if arr[i] == 'f':
            cur_indent += 1
            max_indent += 1
            continue
        cur = [0 for _ in range(indent_num + 1)]
        cal_pref(dp, pref)
        for j in range(cur_indent, indent_num + 1):
            res_idx = j - cur_indent
            res_result = pref[res_idx - 1] if res_idx > 0 else 0
            cur[j] = (pref[indent_num] - res_result) % mod
        cur[max_indent] = 1 if not cur[max_indent] else cur[max_indent]
        dp = cur
        cur_indent = 0

    result = sum(dp) % mod
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模用于实验
    main(10)