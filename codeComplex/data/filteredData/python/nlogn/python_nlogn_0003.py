import random

def main(n):
    # 生成测试数据
    # t 为间距阈值，这里设为 1 到 10 之间的随机整数
    t = random.randint(1, 10)
    cont = []
    for _ in range(n):
        # 生成房屋中心和长度：
        # 中心在 [-100, 100]，长度在 [1, 20]
        house_center = random.randint(-100, 100)
        house_len = random.randint(1, 20)
        cont.append([house_center - house_len / 2, house_center + house_len / 2])

    # 按原逻辑处理
    ans = 2
    cont.sort(key=lambda element: element[0])

    for i in range(0, n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap > t:
            ans += 2
        elif gap == t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例调用：规模 n 可根据需要修改
    main(5)