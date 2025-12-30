import random
import string

def main(n: int):
    """
    n 作为规模参数，这里用作字符串 c 的长度。
    a 固定为 26（字母表长度），b 从 1 到 min(26, n) 中随机生成。
    c 为长度为 n 的随机小写字母串。
    """
    # 生成测试数据
    a = 26
    b = random.randint(1, min(26, max(1, n)))
    c = ''.join(random.choice(string.ascii_lowercase) for _ in range(max(1, n)))

    su = 0
    cnt = 0
    j = -2
    i = 0
    lis = "abcdefghijklmnopqrstuvwxyz"
    while i < 26 and cnt < b:
        if lis[i] in c and i - 2 >= j:
            su += i + 1
            cnt += 1
            j = i
        i += 1
    if cnt < b:
        print(-1)
    else:
        print(su)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改
    main(10)