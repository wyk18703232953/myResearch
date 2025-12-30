import random
import string

def main(n):
    # 生成随机字符串 s, t，长度为 n，保证可以通过相邻交换将 s 变为 t
    # 做法：先生成随机 s，然后对 s 做一系列随机相邻交换得到 t
    letters = string.ascii_lowercase
    s = [random.choice(letters) for _ in range(n)]
    t = s[:]  # 先拷贝
    # 进行若干次随机相邻交换，生成 t
    if n > 1:
        for _ in range(n):  # 交换 n 次，规模适中
            i = random.randint(0, n - 2)
            t[i], t[i + 1] = t[i + 1], t[i]

    # 下面是原逻辑（从 s 变为 t，记录相邻交换操作）
    s = s[:]  # 拷贝一份可变
    t = t[:]
    ans = []

    for i in range(n):
        if s[i] == t[i]:
            continue
        found = False
        for j in range(i + 1, n):
            if s[j] == t[i]:
                found = True
                # 将 s[j] 通过相邻交换移动到位置 i
                for k in range(j, i, -1):
                    s[k - 1], s[k] = s[k], s[k - 1]
                    ans.append(k)
                break
        if not found:
            print(-1)
            return

    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次运行
    main(5)