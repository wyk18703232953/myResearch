def main(n):
    # n 表示数组长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性构造：让每个元素恰好出现两次，方便触发 index/remove 逻辑
    # 例如 n=5 -> [0,1,2,3,4,0,1,2,3,4]
    base = list(range(n))
    arr = base + base

    ans = 0
    # 保持原逻辑：每次弹出一个 e，累加其在剩余数组中的 index，并移除下一次出现的 e
    while len(arr) != 0:
        e = arr.pop(0)
        ans += arr.index(e)
        arr.remove(e)

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)