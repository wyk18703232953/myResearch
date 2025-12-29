import random


def main(n):
    # 生成规模为 n 的测试数据
    # 设置 k，并生成 n 个非负整数
    k = max(1, n // 2)  # 简单示例规则：k 随 n 变化，至少为 1
    v = [random.randint(0, 10 ** 9) for _ in range(n)]

    d = {}
    ans = 0

    # 预处理：按数字位数和 x % k 分组
    for x in v:
        num_d, mod_k = len(str(x)), x % k
        d.setdefault(num_d, {}).setdefault(mod_k, []).append(x)

    # 枚举所有有序对 (x, y)
    for x in v:
        num_d, mod_k = len(str(x)), x % k
        for add, mods in d.items():
            val_mod = (mod_k * pow(10, add, k)) % k
            need_mod = (k - val_mod) % k
            ans += len(mods.get(need_mod, []))
            if need_mod == mod_k and add == num_d:
                ans -= 1

    print(ans)


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)