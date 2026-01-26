def main(n):
    # 确定性生成 n 和 k，以及数组 v
    # 映射：n 为数组长度，k 为与 n 相关的确定性值（保证 >= 2）
    k = max(2, (n % 97) + 2)
    v = [(i * 131 + 7) % (10 ** 9 + 7) for i in range(1, n + 1)]

    d = {}
    ans = 0

    for x in v:
        num_d, mod_k = len(str(x)), x % k
        d.setdefault(num_d, {}).setdefault(mod_k, []).append(x)

    for x in v:
        num_d, mod_k = len(str(x)), x % k
        for add, mods in d.items():
            val_mod = (mod_k * pow(10, add, k)) % k
            need_mod = (k - val_mod) % k
            ans += len(mods.get(need_mod, []))
            if need_mod == mod_k and add == num_d:
                ans -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)