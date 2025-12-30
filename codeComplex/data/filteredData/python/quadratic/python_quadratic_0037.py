def main(n):
    mod = 10 ** 9 + 7

    # 生成测试数据：长度为 n 的由 'f' 和 's' 组成的数组
    # 这里简单生成前半部分为 'f'，后半部分为 's'
    arr = ['f' if i < n // 2 else 's' for i in range(n)]

    indent_num = 0
    for i in range(n):
        if arr[i] == 'f':
            indent_num += 1

    dp = [0 for _ in range(indent_num + 1)]
    max_indent = 0
    cur_indent = 0
    pref = [0 for _ in range(indent_num + 1)]

    def cal_pref(dp_local, pref_local):
        pref_local[0] = dp_local[0]
        for k in range(1, len(dp_local)):
            pref_local[k] = pref_local[k - 1] + dp_local[k]

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

    print(sum(dp) % mod)


if __name__ == "__main__":
    # 示例调用：可以修改 n 观察结果
    main(5)