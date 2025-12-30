import random
import string

def main(n):
    # 1. 生成测试数据
    # 将规模 n 映射为 b（需要选择的字符个数），限制在 1~26 之间
    b = max(1, min(26, n))

    # 随机生成字符串 c，由小写字母组成，长度与 n 相关
    length_c = max(1, n)  # 至少长度为 1
    c = ''.join(random.choice(string.ascii_lowercase) for _ in range(length_c))

    # 2. 原逻辑：在字母表中按顺序选 b 个字符，使得下标差至少为 2，且字符在 c 中出现
    su = 0
    cnt = 0
    j = -2
    i = 0
    lis = "abcdefghijklmnopqrstuvwxyz"

    while i < 26 and cnt < b:
        if lis[i] in c and i - 2 >= j:
            su += i + 1    # 字符位置 i 对应权重 i+1
            cnt += 1
            j = i
        i += 1

    if cnt < b:
        result = -1
    else:
        result = su

    # 为了可复用，返回结果（也可在此处 print）
    return {
        "b": b,
        "c": c,
        "result": result
    }

if __name__ == "__main__":
    # 示例：运行规模 n=10
    out = main(10)
    print(out["result"])