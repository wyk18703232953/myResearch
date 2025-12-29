import random

def main(n):
    # 生成测试数据：n 的规模，k 在 [1, max(1, n//2)]，p 为 0..n-1 的随机排列
    if n <= 0:
        return
    k = random.randint(1, max(1, n // 2))
    p = list(range(n))
    random.shuffle(p)

    ans = [-1] * (max(p) + 1)
    ans[0] = 0
    for i in range(n):
        if ans[p[i]] < 0:
            position = p[i] - k + 1
            for j in range(max(0, p[i] - k + 1), p[i] + 1):
                if ans[j] < 0:
                    position = j
                    break
            j = max(0, position - 1)
            key = ans[j]
            count = 0
            while j >= 0:
                if ans[j] != key:
                    position1 = j + 1  # 保留以贴近原逻辑，虽然后续未使用
                    break
                j -= 1
                count += 1
            if count + p[i] + 1 - position > k:
                key = position
            for j in range(position, p[i] + 1):
                ans[j] = key

    # 输出结果，格式与原程序一致
    for i in range(n):
        if i != len(p) - 1:
            wk1 = " "
        else:
            wk1 = "\n"
        print(ans[p[i]], end=wk1)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)