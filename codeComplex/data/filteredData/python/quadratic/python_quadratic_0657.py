def main(n):
    # 生成确定性测试数据：
    # 解释：我们模拟原程序中的 T 组测试，这里设为 T = n，
    # 每组数据的长度为 m = n，元素依次循环 1..n。
    T = n
    all_cases = []
    for t in range(T):
        m = n
        case = [(i % n) + 1 for i in range(m)]
        all_cases.append(case)

    # 核心算法逻辑保持不变
    for alst in all_cases:
        ans = []
        for a in alst:
            if a == 1:
                ans.append("1")
                # print(".".join(ans))
                pass
                continue
            while ans and int(ans[-1]) != a - 1:
                ans.pop()
            if not ans:
                ans.append(str(a))

            else:
                ans.pop()
                ans.append(str(a))
            # print(".".join(ans))
            pass
if __name__ == "__main__":
    main(5)