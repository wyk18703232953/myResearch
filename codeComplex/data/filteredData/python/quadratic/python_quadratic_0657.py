def main(n):
    # 生成测试数据：长度为 n 的列表，元素在 1..5 之间循环
    # 你可以按需要修改生成策略
    alst = [(i % 5) + 1 for i in range(1, n + 1)]

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
    # 示例：调用 main(10)
    main(10)