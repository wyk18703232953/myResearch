import string
import random

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def main(n):
    # 生成测试数据：随机字符串 a, b，保证是变位词（字符频次相同）
    letters = string.ascii_lowercase
    # 随机生成 a
    a = [random.choice(letters) for _ in range(n)]
    # b 是 a 的乱序版本，保证可变换
    b = a[:]
    random.shuffle(b)

    # 以下是原逻辑
    res_a = dict().fromkeys(list(string.ascii_lowercase), 0)
    res_b = dict().fromkeys(list(string.ascii_lowercase), 0)

    for ch in a:
        res_a[ch] += 1
    for ch in b:
        res_b[ch] += 1

    can = True
    for k in res_a:
        if res_a[k] != res_b[k]:
            can = False
            break

    if not can:
        print(-1)
        return

    ans = []
    for i in range(n):
        if a[i] == b[i]:
            continue
        idx = -1
        for j in range(i + 1, n):
            if a[j] == b[i]:
                idx = j
                break
        for j in range(idx, i, -1):
            ans.append(j)
            swap(a, j, j - 1)

    print(len(ans))
    if ans:
        print(' '.join(map(str, ans)))
    else:
        print()

if __name__ == "__main__":
    # 示例调用，可以修改 n 测试不同规模
    main(5)