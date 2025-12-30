import collections
import random
import string


def main(n: int):
    # 生成测试数据：随机字符串 s，t 为 s 的打乱版本
    # 可根据需要调整字符集和生成规则
    letters = string.ascii_lowercase  # 使用小写字母
    if n <= 0:
        # 无有效规模时，直接返回
        return

    # 生成长度为 n 的随机字符串 s
    s = ''.join(random.choice(letters) for _ in range(n))
    # t 为 s 的随机排列，保证 Counter 相同
    t_list = list(s)
    random.shuffle(t_list)
    t = ''.join(t_list)

    # 原始逻辑开始
    if collections.Counter(s) != collections.Counter(t):
        print(-1)
        return

    sl = list(s)
    st = list(t)
    ans = []
    p = 0
    while sl:
        if sl[0] != st[0]:
            k = sl.index(st[0])
            ans.extend(list(range(k + p, p, -1)))
            sl.pop(k)
            st.pop(0)
        else:
            sl.pop(0)
            st.pop(0)
        p += 1

    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改或移除
    main(5)