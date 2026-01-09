def main(n):
    al = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # 构造三个长度为 l 的字符串，l 由 n 决定
    # 选择 l = max(1, n) 保证长度至少为 1
    l = max(1, n)

    # 设计三种不同结构的字符串，方便保持原逻辑但可规模化
    # s[0]: 重复某个字符，方便出现大计数
    s0 = ("a" * l)
    # s[1]: 周期性分布字符
    s1 = "".join(al[i % len(al)] for i in range(l))
    # s[2]: 另一种周期性分布，反向
    s2 = "".join(al[(len(al) - 1 - i) % len(al)] for i in range(l))

    s = [s0, s1, s2]
    ans = [0] * 3

    for c in al:
        for i in range(3):
            cnt_c = s[i].count(c)
            if cnt_c + n <= l:
                ans[i] = max(ans[i], cnt_c + n)

            else:
                if n == 1 and l == cnt_c:
                    ans[i] = max(ans[i], l - 1)

                else:
                    ans[i] = l

    if (ans[0] == ans[1] and max(ans) == ans[0]) or (ans[1] == ans[2] and max(ans) == ans[1]) or (ans[0] == ans[2] and max(ans) == ans[2]):
        # print("Draw")
        pass
    elif max(ans) == ans[0]:
        # print("Kuro")
        pass
    elif max(ans) == ans[1]:
        # print("Shiro")
        pass

    else:
        # print("Katie")
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)