import random
import string

def tonny(ch):
    return ord(ch) - 96

def solve(n, k, s):
    a = sorted(s)
    a = list(map(tonny, a))
    a = sorted(list(set(a)))
    if not a:
        return -1
    ans = [a.pop(0)]
    k -= 1
    for j in a:
        if j - ans[-1] > 1 and k > 0:
            k -= 1
            ans.append(j)
        if k == 0:
            break
    if k != 0:
        return -1
    else:
        return sum(ans)

def main(n):
    # 随机生成 k（1 到 n 之间）
    k = random.randint(1, n)
    # 生成长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    result = solve(n, k, s)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)