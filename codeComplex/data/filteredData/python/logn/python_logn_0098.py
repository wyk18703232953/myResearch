def main(n: int):
    """
    根据规模 n 生成一组 (l, r)，并运行原逻辑。
    这里简单构造：
      l = 0
      r = n
    （可根据需要自行调整测试数据生成方式）
    """
    l = 0
    r = n

    ls = str(bin(l))[2:]
    rs = str(bin(r))[2:]
    llog = len(ls)
    rlog = len(rs)
    ans = 0

    if llog < rlog:
        z = rlog - 1
        while z > -1:
            ans += 2 ** z
            z -= 1

    else:
        ct = 0
        stringa = ""
        for i in range(len(ls)):
            if ls[i] == rs[i] and ct == 0:
                stringa += ls[i]
            if ls[i] == "0" and rs[i] == "1":
                ct += 1
                stringa += ls[i]
            if ls[i] == "1" and rs[i] == "0":
                stringa += ls[i]
            if ls[i] == rs[i] and ct > 0:
                stringa += str((int(rs[i]) + 1) % 2)
        ans = (int(stringa, 2) ^ r)

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)