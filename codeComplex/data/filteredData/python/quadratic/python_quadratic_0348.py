import random
import string

def main(n: int):
    # 生成长度为 n 的随机小写字母串 s
    s = [random.choice(string.ascii_lowercase) for _ in range(n)]
    # 将 s 打乱作为 t，保证 sorted(s) == sorted(t)
    t = s[:]
    random.shuffle(t)

    i, r = 0, []
    # 和原程序保持一致逻辑
    if sorted(s) != sorted(t):
        print(-1)
        return

    while i < n:
        j = i
        while j < n and s[j] != t[i]:
            j += 1
        s[i:j + 1] = s[j:j + 1] + s[i:j]
        r.extend(range(j, i, -1))
        i += 1

    print(len(r))
    if r:
        print(*r)


if __name__ == '__main__':
    # 示例：调用 main(5) 进行一次运行
    main(5)