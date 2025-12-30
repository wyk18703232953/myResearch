import random

def main(n):
    # 生成一个长度为 n 的随机排列 ans（0 ~ n-1，互不相同）
    ans = list(range(n))
    random.shuffle(ans)

    # 计算 l 和 r
    l = [0] * n
    r = [0] * n
    for i in range(n):
        cnt = 0
        for j in range(i):
            if ans[j] > ans[i]:
                cnt += 1
        l[i] = cnt
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if ans[j] > ans[i]:
                cnt += 1
        r[i] = cnt

    # 使用原逻辑验证 l, r 是否正确，并输出结果
    slr = [l[i] + r[i] for i in range(n)]
    chk_ans = [n - slr[i] for i in range(n)]

    flag = True
    if l[0] != 0 or r[n - 1] != 0:
        flag = False

    for i in range(n):
        great = 0
        for j in range(i + 1, n):
            if chk_ans[i] < chk_ans[j]:
                great += 1
        if r[i] != great:
            flag = False
            break

    for i in range(n - 1, -1, -1):
        great = 0
        for j in range(i - 1, -1, -1):
            if chk_ans[i] < chk_ans[j]:
                great += 1
        if l[i] != great:
            flag = False
            break

    if flag:
        print("YES")
        for i in range(n - 1):
            print(chk_ans[i], end=" ")
        print(chk_ans[n - 1])
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的测试数据并运行
    main(5)