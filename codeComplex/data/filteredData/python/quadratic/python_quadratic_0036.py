def main(n):
    # 生成测试数据：长度为 n 的指令序列，只包含 'f' 或 's'
    # 这里简单生成前 n//2 个为 'f'，后面为 's'，可按需要自行修改
    arr = []
    for i in range(n):
        if i < n // 2:
            arr.append('f')
        else:
            arr.append('s')

    mod = 10 ** 9 + 7
    indent_num = 0

    # 统计所有行中 'f' 的数量
    for i in range(n):
        if arr[i] == 'f':
            indent_num += 1

    dp = [0 for _ in range(indent_num + 1)]
    first_block_index = 0
    max_indent = 0

    # 前缀连续的 'f' 的数量
    for x in arr:
        if x != 'f':
            break
        first_block_index += 1
        max_indent += 1

    dp[max_indent] = 1
    cur_indent = 0
    pref = [0 for _ in range(indent_num + 1)]

    def cal_pref(dp_list, pref_list):
        pref_list[0] = dp_list[0]
        for i in range(1, len(dp_list)):
            pref_list[i] = pref_list[i - 1] + dp_list[i]

    for i in range(first_block_index + 1, n):
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
        # 保留初始块的状态
        cur[max_indent] = 1 if not cur[max_indent] else cur[max_indent]
        dp = cur
        cur_indent = 0

    return sum(dp) % mod


if __name__ == "__main__":
    # 示例：调用 main(5)，真实使用时可按需调整 n
    result = main(5)
    print(result)