import random
import string

def main(n):
    # 生成测试数据：长度为 n 的两个字符串 s, d
    # 保证 sorted(s) == sorted(d)，以避免直接输出 -1
    if n <= 0:
        return

    # 示例生成策略：从小写字母中随机选取字符
    chars = [random.choice(string.ascii_lowercase) for _ in range(n)]
    s = chars[:]                 # 初始字符串 s
    d = chars[:]                 # d 是 s 的一个打乱版本
    random.shuffle(d)

    s = list(s)
    d = list(d)

    if sorted(s) != sorted(d):
        print(-1)
        return

    ans = []
    for i in range(n):
        if s[i] != d[i]:
            ind = -1
            for u in range(i + 1, n):
                if s[u] == d[i]:
                    ind = u
                    break
            if ind == -1:
                print(-1)
                return

            cnt = abs(ind - i)
            s.pop(ind)
            s.insert(i, d[i])

            for _ in range(cnt):
                if ind > 0:
                    ans.append(ind)
                else:
                    ans.append(1)
                ind -= 1

    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次测试
    main(5)