import random
import string

def main(n: int):
    # 生成测试数据：随机字符串 s, t，长度为 n，由小写字母组成
    letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    s = [random.choice(letters) for _ in range(n)]
    t = [random.choice(letters) for _ in range(n)]

    d = {}
    ans = 0
    x, y = -1, -1

    # 统计不同位置并记录映射
    for i in range(n):
        if s[i] != t[i]:
            d[(s[i], t[i])] = i
            ans += 1

    l = [chr(i + 97) for i in range(26)]

    # 尝试寻找 (i, j) 与 (j, i) 的互换对，最优可减少 2
    for i in l:
        for j in l:
            if (i, j) in d and (j, i) in d:
                ans -= 2
                x = d[(i, j)] + 1
                y = d[(j, i)] + 1
                break
        if x != -1:
            break

    # 如果没找到互换对，则尝试寻找链 (i, j), (j, k)，可减少 1
    if x == y == -1:
        for i in l:
            for j in l:
                for k in l:
                    if (i, j) in d and (j, k) in d:
                        ans -= 1
                        x = d[(i, j)] + 1
                        y = d[(j, k)] + 1
                        break
                if x != -1:
                    break
            if x != -1:
                break

    # 输出结果
    print(ans)
    print(x, y)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)