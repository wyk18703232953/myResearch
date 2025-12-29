#!/usr/bin/env python3

import random
import string


def solve_case(s: str, t: str) -> bool:
    s_list = list(s)
    t_list = list(t)
    ok = False
    for i in range(len(t_list)):
        t1 = list(t_list[:i]) + ["#"]
        t2 = list(t_list[i:]) + ["#"]
        # dp[seen i-th index][match j in front] = match in back
        dp = [[-1] * (len(t_list) + 1) for _ in range(len(s_list) + 1)]
        dp[0][0] = 0
        for j, ch in enumerate(s_list):
            for k in range(len(t1)):
                if dp[j][k] == -1:
                    continue
                # 不用当前字符
                dp[j + 1][k] = max(dp[j + 1][k], dp[j][k])
                # 匹配前半部分 t1
                if ch == t1[k]:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k])
                # 匹配后半部分 t2
                if ch == t2[dp[j][k]]:
                    dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + 1)
        for k in range(len(t_list) + 1):
            if dp[len(s_list)][k] + k >= len(t_list):
                ok = True
                break
        if ok:
            break
    return ok


def generate_test_case(n: int) -> tuple[str, str]:
    """
    根据规模 n 生成一组 (s, t).
    这里简单设置：
      - |t| = max(1, n // 3)
      - |s| = max(|t|, n)
      - 字符集使用 'a'~'c'
    """
    alpha = "abc"
    len_t = max(1, n // 3)
    len_s = max(len_t, n)

    t = "".join(random.choice(alpha) for _ in range(len_t))

    # 生成 s：大概率包含 t 的子序列结构，也可能不包含
    s = []
    i = 0
    while len(s) < len_s:
        if i < len_t and random.random() < 0.6:
            s.append(t[i])
            i += 1
        else:
            s.append(random.choice(alpha))
    s = "".join(s)
    return s, t


def main(n: int):
    """
    n 为规模参数，用于控制生成的数据长度。
    这里生成 1 个测试用例并输出 YES/NO。
    """
    random.seed(0)
    s, t = generate_test_case(n)
    ok = solve_case(s, t)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    # 示例：规模 100
    main(100)