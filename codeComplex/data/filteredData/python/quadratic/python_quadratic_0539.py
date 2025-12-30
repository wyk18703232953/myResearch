import random

def main(n: int):
    # 生成测试数据：n 个随机正整数（1~n），作为原程序中的 l
    # 这里可以根据需要调整数据生成策略
    l = [random.randint(1, n) for _ in range(n)]

    # 下面是原逻辑，只是去掉了 input()，并封装到 main 中
    ll = []
    res = []
    head = 0
    dia = 0

    for i in range(1, n):
        if l[i] == 1:
            l[i] = 0
            ll.append(i)
        else:
            res.append((head + 1, i + 1))
            l[head] -= 1
            dia += 1
            head = i
            l[head] -= 1

    if l[head] > 0 and len(ll) > 0:
        res.append((ll[0] + 1, head + 1))
        l[head] -= 1
        del ll[0]
        dia += 1

    if l[0] > 0 and len(ll) > 0:
        res.append((ll[0] + 1, 1))
        l[0] -= 1
        del ll[0]
        dia += 1

    for i in ll:
        for j in range(n):
            if l[j] > 0:
                res.append((j + 1, i + 1))
                l[j] -= 1
                break

    if len(res) < n - 1:
        print("NO")
    else:
        print("YES " + str(dia))
        print(n - 1)
        for p in res:
            print(p[0], p[1])


if __name__ == "__main__":
    # 示例：运行 main(5)，可根据需要修改或由外部调用 main(n)
    main(5)