def main(n):
    # Interpret n as both the size of the list v and the value of k (to scale together deterministically)
    if n <= 0:
        # print(0)
        pass
        return

    k = max(1, n)  # ensure k >= 1

    # Deterministically generate v of length n
    # Use simple arithmetic patterns based on n and index
    # Values will vary with n but remain fully deterministic
    v = [(i * i + 3 * i + 7) % (10 * k + 1) + 1 for i in range(n)]

    d = {}
    ans = 0

    for x in v:
        num_d, mod_k = len(str(x)), x % k
        d.setdefault(num_d, {}).setdefault(mod_k, []).append(x)

    for x in v:
        num_d, mod_k = len(str(x)), x % k
        for add, mods in d.items():
            val_mod = (mod_k * 10 ** add) % k
            need_mod = (k - val_mod) % k
            ans += len(mods.get(need_mod, []))
            if need_mod == mod_k and add == num_d:
                ans -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)