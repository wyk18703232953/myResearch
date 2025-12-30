import sys
import random

def main(n: int):
    # 生成一组满足条件的 res（1..n 的排列）
    res = list(range(1, n + 1))
    random.shuffle(res)

    # 根据 res 生成 l 和 r
    l = [0] * n
    r = [0] * n
    for i in range(n):
        left_cnt = 0
        for j in range(i):
            if res[j] > res[i]:
                left_cnt += 1
        l[i] = left_cnt

        right_cnt = 0
        for j in range(i + 1, n):
            if res[j] > res[i]:
                right_cnt += 1
        r[i] = right_cnt

    # 使用原逻辑验证并输出
    calc_res = [0] * n
    for i in range(n):
        calc_res[i] = n - l[i] - r[i]

    for i in range(n):
        ok = 0
        for j in range(i):
            if calc_res[j] > calc_res[i]:
                ok += 1
        if ok != l[i]:
            print("NO")
            return
        ok = 0
        for j in range(i + 1, n):
            if calc_res[j] > calc_res[i]:
                ok += 1
        if ok != r[i]:
            print("NO")
            return

    print("YES")
    print(" ".join(map(str, calc_res)))

if __name__ == "__main__":
    # 示例：可以在此处调用 main 进行简单测试
    # 比如 n = 5
    main(5)