import random
import string


def main(n: int):
    # 1. 生成测试数据
    # a: 长度为 n 的数字字符列表
    # b: 长度为 n 的数字字符串
    digits = string.digits
    a = [random.choice(digits) for _ in range(n)]
    b = ''.join(random.choice(digits) for _ in range(n))

    # 打印测试数据（如不需要可注释掉）
    # print("a_src:", ''.join(a))
    # print("b_src:", b)

    # 2. 原逻辑开始
    out = []
    mx = '/'
    a.sort()
    a.reverse()
    x = len(a)

    if x == len(b):
        for i in range(x):
            q = 0
            for j in range(len(a)):
                if a[j] == b[i]:
                    out.append(a[j])
                    a.pop(a.index(a[j]))
                    q = 1
                    break
                elif a[j] < b[i]:
                    out.append(a[j])
                    a.pop(a.index(a[j]))
                    print(''.join(out), end='')
                    print(''.join(a))
                    return
            if q == 0:
                break
        if q == 1:
            print(''.join(out))
        else:
            y = len(out)
            for i in range(y - 1, -1, -1):
                for j in range(len(a)):
                    if a[j] < b[i] and a[j] > mx:
                        mx = a[j]
                if mx != '/':
                    a.append(out[len(out) - 1])
                    out.pop()
                    out.append(mx)
                    a.pop(a.index(mx))
                    a.sort()
                    a.reverse()
                    print(''.join(out), end='')
                    print(''.join(a))
                    return
                else:
                    a.append(out[len(out) - 1])
                    out.pop()
                    a.sort()
                    a.reverse()

            a.pop(a.index(mx))
            print(mx, end='')
            print(''.join(a))
    else:
        print(''.join(a))


if __name__ == "__main__":
    # 示例：n = 8，对应原代码注释中的示例长度
    main(8)