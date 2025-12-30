import random
import string

def counter(s, x):
    p = len(x)
    px = 0
    for i in range(len(s)):
        if s[i:i + p] == x:
            px += 1
    return px

def main(n):
    # 生成长度为 n 的随机小写字母字符串作为测试数据
    # 可根据需要调整字符集
    chars = string.ascii_lowercase
    arr = ''.join(random.choice(chars) for _ in range(n))

    ms = ""
    mn = 0

    for i in range(n):
        s = ""
        for j in range(i, n):
            s += arr[j]
            c = counter(arr, s)
            if c > 1 and len(s) > mn:
                ms = s
                mn = len(s)

    print(mn)

if __name__ == "__main__":
    # 示例：调用 main(10)，可自行修改 n 的大小
    main(10)