def main(n):
    mod = 10**9 + 7

    # 构造确定性的输入：长度为 n 的字符串序列，由 'f' 和 's' 组成
    # 这里让前 n//3 个为 'f'，其余为 's'，并在剩余部分以 2 为周期交替
    arr = []
    for i in range(n):
        if i < n // 3:
            arr.append('f')

        else:
            if (i - n // 3) % 2 == 0:
                arr.append('s')

            else:
                arr.append('f')

    indent_num = 0
    for i in range(n):
        if arr[i] == 'f':
            indent_num += 1

    dp = [0 for _ in range(indent_num + 1)]
    first_block_index = 0
    max_indent = 0
    for x in arr:
        if x != 'f':
            break
        first_block_index += 1
        max_indent += 1

    if max_indent <= indent_num:
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
        if max_indent <= indent_num:
            cur[max_indent] = 1 if not cur[max_indent] else cur[max_indent]
        dp = cur
        cur_indent = 0

    return sum(dp) % mod


if __name__ == "__main__":
    # 示例调用，可以根据需要修改 n 以进行规模实验
    # print(main(10))
    pass