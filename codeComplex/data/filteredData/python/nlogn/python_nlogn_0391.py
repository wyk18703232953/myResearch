import random

def main(n):
    # 生成参数 k，范围 [0, n]，可按需调整策略
    k = random.randint(0, n)

    # 生成长度为 n 的数组 a、b，元素范围可按需调整
    a = [random.randint(1, 100) for _ in range(n)]
    b = [random.randint(1, 100) for _ in range(n)]

    c = list(sorted(zip(a, b, range(len(b)))))
    d = [0] * len(b)

    if k == 0:
        print(' '.join(map(str, b)))
    else:
        best = [0] * k
        for pwr, cnt, index in c:
            d[index] = sum(best) + cnt

            if cnt > best[0]:
                for i in range(len(best)):
                    if cnt <= best[i]:
                        best.insert(i, cnt)
                        best = best[1:]
                        break
                else:
                    best = best[1:] + [cnt]

        print(' '.join(map(str, d)))


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)