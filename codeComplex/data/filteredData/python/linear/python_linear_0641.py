import random

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素为正整数，至少保证存在一个 >1 的元素（若可能）
    if n <= 0:
        print("NO")
        return

    a = [1] * n
    if n >= 1:
        # 随机选一些位置改为 >1
        for i in range(n):
            if random.random() < 0.3:  # 30% 概率设为 >1
                a[i] = random.randint(2, 5)

        # 确保不是全 1（如果希望更覆盖原逻辑）
        if all(x == 1 for x in a) and n > 1:
            pos = random.randrange(n)
            a[pos] = random.randint(2, 5)

    # 原逻辑开始
    os = 0
    oss = []
    nos = 0
    nos_0 = -1
    nos_1 = -1
    sumnos = 0

    for i in range(n):
        if a[i] == 1:
            os += 1
            oss.append(i + 1)
        else:
            sumnos += a[i]
            nos += 1
            if nos_0 == -1:
                nos_0 = i + 1
            nos_1 = i + 1

    if os <= sumnos - (2 * (nos - 1)):
        es = []
        oss_i = 0
        ans = nos - 1
        if os >= 1:
            ans += 1
            es.append((nos_0, oss[0]))
            oss_i += 1
        if os >= 2:
            ans += 1
            es.append((nos_1, oss[1]))
            oss_i += 1
        print("YES", ans)
        prev_nos = -1
        for i in range(n):
            if a[i] > 1:
                if prev_nos != -1:
                    es.append((prev_nos + 1, i + 1))
                for _ in range(a[i] - 2):
                    if oss_i >= os:
                        break
                    es.append((i + 1, oss[oss_i]))
                    oss_i += 1
                prev_nos = i
        print(len(es))
        for e in es:
            print(*e)
    else:
        print("NO")


# 示例调用
if __name__ == "__main__":
    main(5)