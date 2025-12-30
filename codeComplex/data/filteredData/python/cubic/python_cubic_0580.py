import sys
import random

def countdig(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

def findmin(h, arr):
    arr.sort()
    h = int(h)
    ans = '-1'
    for i in arr:
        if int(i) > h:
            break
        ans = i
    return ans

def main(n):
    # 1. 根据规模 n 生成测试数据
    # 生成一个目标串 n1，长度为 n，数字在 0-9
    # 然后生成 n，使得 n 的长度在 [1, len(n1)]，数字同样在 0-9
    length_n1 = max(1, n)            # 保证长度至少为 1
    length_n = random.randint(1, length_n1)

    n1 = ''.join(str(random.randint(0, 9)) for _ in range(length_n1))
    n_list = list(''.join(str(random.randint(0, 9)) for _ in range(length_n)))

    # 将生成的 n1 打印到 stderr，方便测试时观察输入（不影响原逻辑输出）
    # 也可以注释掉这两行
    print(f"Generated n1: {n1}", file=sys.stderr)
    print(f"Generated n : {''.join(n_list)}", file=sys.stderr)

    n_chars = n_list
    n1_chars = list(n1)

    if len(n_chars) < len(n1_chars):
        n_chars.sort(reverse=True)
        print(''.join(n_chars))
        return

    n_chars.sort()
    ans = ""
    f = 0
    for i in range(len(n_chars)):
        t = i - 1
        c = 0
        r = findmin(n1_chars[i], n_chars)
        if r == '-1':
            while r == '-1':
                n_chars.append(ans[-c - 1])
                r = findmin(int(n1_chars[t]) - 1, n_chars)
                t -= 1
                c += 1
            ans = ans[:len(ans) - c]
            ans += r
            n_chars.remove(r)
            f = 1
            break
        n_chars.remove(r)
        if r == n1_chars[i]:
            ans += r
            continue
        else:
            ans += r
            f = 1
            break
    if f == 1:
        n_chars.sort(reverse=True)
        for i in n_chars:
            ans += i
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)