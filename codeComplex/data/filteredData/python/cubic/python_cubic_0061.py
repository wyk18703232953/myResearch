import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字母串
    #    可根据需要修改字符集或生成规则
    x = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

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
                c = 0
                ans = 0
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
    # 示例：规模为 20
    main(20)