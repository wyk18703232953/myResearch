import random
import string


def main(n: int):
    # 生成测试数据：随机字符串 s, t，保证 sorted(s) == sorted(t)
    # 字符集使用小写字母
    letters = string.ascii_lowercase
    # 随机生成 s
    s = [random.choice(letters) for _ in range(n)]
    # t 为 s 的随机重排（保证是同构）
    t = s[:]
    random.shuffle(t)
    t = ''.join(t)

    # 下面是原逻辑，只是去掉了 input 并用生成的 s, t
    s_work = s[:]  # 工作副本，按原代码行为是 list
    if sorted(s_work) != sorted(t):
        print(-1)
        return

    lst = [0] * n
    for i in range(n):
        for j in range(n):
            if s_work[j] == t[i]:
                lst[j] = i + 1
                s_work[j] = "."
                break

    ans = 0
    a = []
    for i in range(n):
        for j in range(n - 1):
            if i != j:
                if lst[j] > lst[j + 1]:
                    ans += 1
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    a.append(j + 1)

    print(ans)
    if ans > 0:
        print(*a)


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改规模
    main(5)