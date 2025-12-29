import random
import string

def main(n):
    # 生成测试数据
    # 生成两个长度为 n 的小写字母串 a, b
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    b = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    num = n
    dic = {}
    lis = []
    ham = 0
    swap1 = -1
    swap2 = -1
    p = False
    q = False

    for i in range(num):
        if a[i] != b[i]:
            ham += 1
            lis.append(i)
            dic[b[i]] = i

    for i in lis:
        if a[i] in dic:
            p = True
            swap1 = i + 1
            f = dic[a[i]]
            swap2 = f + 1
            if a[f] == b[i]:
                q = True
                break

    print(ham - (2 if q else 1 if p else 0))
    print(swap1, swap2)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)