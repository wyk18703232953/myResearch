import random

def main(n):
    # 生成测试数据
    # 这里生成 n 个在 [1, 10^6] 之间的随机整数作为 num
    num = [random.randint(1, 10**6) for _ in range(n)]
    # 生成 l, r, x，使得有一定概率存在可行解
    total_sum = sum(num)
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    r = random.randint(l, total_sum if total_sum > 0 else l)
    x = random.randint(0, max(num) - min(num) if n > 1 else 0)

    ans = 0
    for mask in range(1 << n):
        st = bin(mask)[2:].zfill(n)
        if st.count('1') >= 2:
            pt = []
            for i in range(n):
                if st[i] == '1':
                    pt.append(num[i])
            s = sum(pt)
            if l <= s <= r and max(pt) - min(pt) >= x:
                ans += 1

    print(ans)
    # 如果需要也可以返回结果和测试数据
    return ans, num, l, r, x


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)