M = 0x3b800001
wa = 0

def main(n):
    global wa
    wa = 0
    if n <= 0:
        # print(0)
        pass
        return
    # 确定性生成长度为 n 的数组 a
    a = [(i * 2 + 1) % M for i in range(n)]
    now = 1
    wa_local = 0
    wa_local += a[-1]
    for i in range(n - 1)[::-1]:
        wa_local += (now * (n - i - 1) + now * 2) * a[i]
        wa_local %= M
        now *= 2
        now %= M
    wa_local %= M
    wa = wa_local
    # print(wa_local)
    pass
if __name__ == "__main__":
    main(5)