import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：
    #    这里用 n 作为数值上界，在 [0, n] 内随机生成 a, b
    #    你也可以根据需要改成确定性构造，如 a = n//2, b = n
    a = random.randint(0, n)
    b = random.randint(0, n)

    # 原逻辑开始
    a, b = min(a, b), max(a, b)

    bina = str(bin(a))[2:]
    binb = str(bin(b))[2:]

    lena = len(bina)
    lenb = len(binb)

    ans = 0
    if lena != lenb:
        ans = 2 ** lenb - 1
    else:
        # 注意：原代码此处给 a 赋值了字符串，但实际使用的是 bina/binb
        a_str = '0' * (lena - lenb) + bina  # 保留原意，变量名改为 a_str
        for i in range(lenb):
            if (bool(int(bina[i])) != bool(int(binb[i]))):
                ans = 2 ** (lenb - i) - 1
                break

    print(ans)


# 示例：直接运行本文件时，以 n = 10 为规模调用
if __name__ == "__main__":
    main(10)