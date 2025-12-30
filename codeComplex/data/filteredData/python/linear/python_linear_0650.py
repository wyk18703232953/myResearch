import random

def main(n):
    # 随机生成 c（值域与原代码中 cnt 数组长度一致）
    MAXV = 500000
    c = random.randint(1, min(MAXV, max(1, n)))  # 保证 c 在合理范围内
    
    # 生成长度为 n 的数组，元素范围 [1, MAXV]
    arr = [random.randint(1, MAXV) for _ in range(n)]

    cnt = [0] * (MAXV + 5)
    ans = 0

    for v in arr:
        if v == c:
            cnt[c] += 1
        else:
            if cnt[v] < cnt[c]:
                cnt[v] = cnt[c]
            cnt[v] += 1
        ans = max(ans, cnt[v] - cnt[c])

    print(ans + cnt[c])


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)