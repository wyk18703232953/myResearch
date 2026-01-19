def main(n):
    # n 表示字符串长度规模
    # 构造确定性输入：
    # 原程序有两行输入：第一行是目标串 n，第二行是模式串 s
    # 这里把两者都构造为长度 n 的由 '+' 和 '-' 组成的串，其中 s 中前半段用 '?' 替代，产生不确定位置
    if n <= 0:
        return

    # 构造原来的 n 字符串：交替 '+' 和 '-'
    target = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    # 构造原来的 s 字符串：
    # 前 n//3 个字符固定为 target 的对应字符
    # 中间 n//3 个字符为 '?'
    # 剩余字符为 target 的反号
    part = n // 3
    fixed_prefix = target[:part]
    question_part = '?' * part
    suffix_len = n - 2 * part
    fixed_suffix = ''.join('+' if target[2 * part + i] == '-' else '-' for i in range(suffix_len))
    s = fixed_prefix + question_part + fixed_suffix

    quest = s.count("?")
    plusn = target.count("+")
    plus = s.count("+")

    from math import factorial as f

    try:
        need = plusn - plus
        if need < 0 or need > quest:
            raise ValueError
        comb = f(quest) / (f(need) * f(quest - need))
        ans = comb / (2 ** quest)
        print(f"{ans:.12f}")
    except Exception:
        print(f"{0.0:.12f}")


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模调用
    main(10)