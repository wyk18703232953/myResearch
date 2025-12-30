import random
import string


def main(n: int):
    # 生成规模为 n 的测试数据（3 个长度为 l 的字符串）
    # 这里令字符串长度 l 与 n 相关，例如 l = max(1, n)
    l = max(1, n)
    al = list(string.ascii_lowercase + string.ascii_uppercase)

    # 随机生成 3 行字符串，每行长度为 l，字符从 al 中采样
    s = [
        "".join(random.choice(al) for _ in range(l))
        for _ in range(3)
    ]

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

    if (
        (ans[0] == ans[1] and max(ans) == ans[0])
        or (ans[1] == ans[2] and max(ans) == ans[1])
        or (ans[0] == ans[2] and max(ans) == ans[2])
    ):
        print("Draw")
    elif max(ans) == ans[0]:
        print("Kuro")
    elif max(ans) == ans[1]:
        print("Shiro")
    else:
        print("Katie")


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(5)