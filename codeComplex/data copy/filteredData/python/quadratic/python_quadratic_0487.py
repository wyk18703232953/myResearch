def main(n):
    if n <= 0:
        return

    # 构造一个确定性的 ans 序列：例如等差序列
    # ans[i] = i（0 到 n-1）
    ans = [i for i in range(n)]

    # 由 ans 反推原程序中需要的 l, r
    # l[i] = 在 ans[0..i-1] 中，比 ans[i] 大的元素个数
    # r[i] = 在 ans[i+1..n-1] 中，比 ans[i] 大的元素个数
    l = [0] * n
    r = [0] * n

    # 计算 l
    for i in range(n):
        cnt = 0
        for j in range(i - 1, -1, -1):
            if ans[i] < ans[j]:
                cnt += 1
        l[i] = cnt

    # 计算 r
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if ans[i] < ans[j]:
                cnt += 1
        r[i] = cnt

    # 按原程序逻辑检查并输出
    slr = [l[i] + r[i] for i in range(n)]
    ans_check = [n - slr[i] for i in range(n)]

    flag = True
    if l[0] != 0 or r[n - 1] != 0:
        flag = False

    for i in range(n):
        great = 0
        for j in range(i + 1, n):
            if ans_check[i] < ans_check[j]:
                great += 1
        if r[i] != great:
            flag = False
            break

    for i in range(n - 1, -1, -1):
        great = 0
        for j in range(i - 1, -1, -1):
            if ans_check[i] < ans_check[j]:
                great += 1
        if l[i] != great:
            flag = False
            break

    if flag:
        # print("YES")
        pass
        for i in range(0, n - 1):
            # print(ans_check[i], end=" ")
            pass
        # print(ans_check[n - 1])
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 以进行规模实验
    main(10)