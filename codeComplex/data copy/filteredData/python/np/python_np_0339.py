import string
from math import inf
from functools import lru_cache

user_masks = [0 for _ in range(1 << 10)]
pizzas = [[] for _ in range(1 << 10)]


def to_bits(l):
    ans = 0
    for i in l:
        ans |= (1 << (i - 1))
    return ans


@lru_cache()
def count_sat_users(mask):
    ans = 0
    cmask = mask
    while cmask:
        ans += user_masks[cmask]
        cmask = (cmask - 1) & mask
    return ans


def generate_input(n):
    # n controls both number of users and pizzas
    if n <= 0:
        n = 1
    max_topping = 9  # use 9 toppings, masks up to (1<<9)-1

    users = []
    pizzas_data = []

    # generate users
    for i in range(n):
        # make each user like between 1 and 9 toppings deterministically
        k = (i % max_topping) + 1
        toppings = [((i + j) % max_topping) + 1 for j in range(k)]
        users.append([k] + toppings)

    # generate pizzas
    for i in range(n):
        # cost is deterministic and growing
        c = (i % 7) + (i // 7) + 1
        k = ((i * 2) % max_topping) + 1
        toppings = [((i * 3 + j) % max_topping) + 1 for j in range(k)]
        pizzas_data.append([c, k] + toppings)

    return n, n, users, pizzas_data


def main(n):
    # reset global state for repeatability
    global user_masks, pizzas
    user_masks = [0 for _ in range(1 << 10)]
    pizzas = [[] for _ in range(1 << 10)]
    count_sat_users.cache_clear()

    n_users, m_pizzas, users, pizzas_data = generate_input(n)

    for row in users:
        k = row[0]
        a = row[1:1 + k]
        bits = to_bits(a)
        user_masks[bits] += 1

    ans = (float(-inf), float(inf), -1, -1)

    for i, row in enumerate(pizzas_data):
        c = row[0]
        k = row[1]
        a = row[2:2 + k]
        bits = to_bits(a)
        pizzas[bits].append((c, i + 1, bits))
        pizzas[bits].sort()
        while len(pizzas[bits]) > 2:
            pizzas[bits].pop()

    for mask_F in range(1 << 9):
        for mask_S in range(1 << 9):
            if len(pizzas[mask_F]) and len(pizzas[mask_S]) and mask_F != mask_S:
                mask = mask_F | mask_S
                satisfied_users = count_sat_users(mask)

                f_pizza = next(iter(pizzas[mask_F]))
                s_pizza = next(iter(pizzas[mask_S]))

                summary_cost = f_pizza[0] + s_pizza[0]

                ans = max(
                    ans,
                    (satisfied_users, -summary_cost, s_pizza[1], f_pizza[1]),
                )

                bmask = mask
                while bmask:
                    satisfied_users += user_masks[bmask]
                    bmask = (bmask - 1) & mask

            if len(pizzas[mask_F]) == 2:
                satisfied_users = count_sat_users(mask_F)

                it = iter(pizzas[mask_F])

                f_pizza = next(it)
                s_pizza = next(it)
                summary_cost = f_pizza[0] + s_pizza[0]
                ans = max(
                    ans,
                    (satisfied_users, -summary_cost, s_pizza[1], f_pizza[1]),
                )

            if len(pizzas[mask_S]) == 2:
                satisfied_users = count_sat_users(mask_S)

                it = iter(pizzas[mask_S])

                f_pizza = next(it)
                s_pizza = next(it)
                summary_cost = f_pizza[0] + s_pizza[0]
                ans = max(
                    ans,
                    (satisfied_users, -summary_cost, s_pizza[1], f_pizza[1]),
                )

    aans = [ans[2], ans[3]]
    aans.sort()
    print(*aans, sep=' ')


if __name__ == "__main__":
    main(10)