import random
import string

def main(n: int):
    # 生成长度为 n 的随机小写字符串 s 和 t
    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for _ in range(n))
    t = ''.join(random.choice(letters) for _ in range(n))

    dic, diff = {}, []
    res, res1, res2 = 0, -1, -1

    for i in range(n):
        if s[i] != t[i]:
            res += 1
            diff.append(i)
            dic[t[i]] = i

    swap1, swap2 = False, False
    for i in diff:
        if s[i] in dic:
            swap1 = True
            res1 = i + 1
            j = dic[s[i]]
            res2 = j + 1
            if s[j] == t[i]:
                swap2 = True
                break

    print(res - (2 if swap2 else 1 if swap1 else 0))
    print(res1, res2)


# 示例：调用 main(10)
if __name__ == "__main__":
    main(10)