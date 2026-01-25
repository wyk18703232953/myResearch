import sys

def main(n):
    if n <= 0:
        print(0)
        return
    # 构造长度为 n 的串，由 'H' 和 'T' 组成，确定性生成
    s = ''.join('H' if i % 2 == 0 else 'T' for i in range(n))
    s += s
    h = 0
    for i in range(n):
        if s[i] == 'H':
            h += 1
    ans = h
    for i in range(n):
        c = 0
        for j in range(i, i + h):
            if s[j] == 'T':
                c += 1
        if c < ans:
            ans = c
    print(ans)

if __name__ == "__main__":
    main(10)