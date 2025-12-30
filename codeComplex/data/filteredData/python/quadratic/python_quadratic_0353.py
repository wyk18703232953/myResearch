import random
import string

def main(n: int):
    # 生成测试数据：随机字符串 s 和 t
    # 约定：始终构造可行解（t 为 s 的乱序）
    if n <= 0:
        return

    # 随机生成 s，由小写字母组成
    letters = string.ascii_lowercase
    s = [random.choice(letters) for _ in range(n)]

    # t 为 s 的随机排列
    t = s[:]  # 先拷贝
    random.shuffle(t)

    # 以下为原逻辑的封装
    if sorted(t) == sorted(s):
        ans = []
        s_work = s[:]  # 在副本上操作，避免修改原始测试数据
        for i in range(n - 1, -1, -1):
            if t[i] != s_work[i]:
                j = s_work.index(t[i])
                for k in range(j, i):
                    s_work[k], s_work[k + 1] = s_work[k + 1], s_work[k]
                    ans.append(str(k + 1))
        print(len(ans))
        if ans:
            print(' '.join(ans))
    else:
        # 按题意，如不可通过交换得到，则输出 -1
        print(-1)


if __name__ == "__main__":
    # 示例：可在此处调用 main 进行简单测试
    main(5)