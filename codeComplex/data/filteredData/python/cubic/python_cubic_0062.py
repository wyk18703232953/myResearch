import random
import string

def main(n: int):
    # 1. 生成规模为 n 的测试数据：由小写字母组成的随机字符串
    #    你也可以根据需要修改字符集
    chars = string.ascii_lowercase
    x = ''.join(random.choice(chars) for _ in range(n))

    # 2. 原始逻辑：求字符串中任意两处相同起始字符的最长公共前缀长度
    l = len(x)
    m = 0
    for i in range(l - 1):
        f = i
        while True:
            idx = x[f + 1:].find(x[f])
            if idx == -1:
                break
            else:
                idx += f + 1
                c = ans = 0
                for j in range(idx, l):
                    if x[j] == x[i + c]:
                        ans += 1
                        c += 1
                    else:
                        break
                if m < ans:
                    m = ans
                f = idx
    print(m)

if __name__ == "__main__":
    # 示例：规模 n=100，可按需修改
    main(100)