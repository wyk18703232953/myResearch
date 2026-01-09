def main(n):
    # 生成确定性的输入：长度为 n 的整数列表
    # 元素构造方式：a[i] = i // 2，保证有大量重复元素，方便触发 index 操作
    a = [i // 2 for i in range(n)]

    ans = 0
    # 保持原逻辑：每次弹出首元素 c，找到列表中第一个等于 c 的元素下标 i，加到 ans，并删除该元素
    # 注意：若列表中不存在 c，会抛出 ValueError，与原行为一致
    while len(a) > 0:
        c = a.pop(0)
        i = a.index(c)
        ans += i
        del a[i]

    return ans


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的取值
    # print(main(10))
    pass