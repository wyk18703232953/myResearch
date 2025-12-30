#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def ilya_and_bank_account(n: int) -> int:
    if n > 0:
        return n
    s = str(n)
    if s[-1] < s[-2] and s[-2] != '0':
        return int(s[:-2] + s[-1:])
    else:
        return int(s[:-1])


def pashmak_and_garden(x1, y1, x2, y2):
    l = abs(x1 - x2)
    m = abs(y1 - y2)
    if x1 == x2:
        return (x1 + m, y1, x2 + m, y2)
    elif y1 == y2:
        return (x1, y1 + l, x2, y2 + l)
    elif l != m:
        return -1
    else:
        return (x1, y2, x2, y1)


def dragons(s: int, pairs):
    sets_ = list(pairs)
    sets_.sort(key=lambda x: x[0])
    for ith, bonus in sets_:
        if ith < s:
            s += bonus
        else:
            return "NO"
    return "YES"


def favorite_sequence(arr):
    ans = []
    start = 0
    end = len(arr) - 1
    while start <= end:
        if start != end:
            ans.append(arr[start])
            ans.append(arr[end])
        else:
            ans.append(arr[end])
        start += 1
        end -= 1
    return ans


def last_years_substring(s: str) -> str:
    n = len(s)
    if s[0] + s[1] == '20' and s[-2] + s[-1] == '20':
        return "YES"
    elif s[0] == '2' and s[-3] + s[-2] + s[-1] == '020':
        return "YES"
    elif s[0] + s[1] + s[2] == '202' and s[-1] == '0':
        return "YES"
    elif s[0] + s[1] + s[2] + s[3] == '2020':
        return "YES"
    elif s[-4] + s[-3] + s[-2] + s[-1] == '2020':
        return "YES"
    else:
        return "NO"


def devu_and_churu_party(n, d, l):
    if (sum(l) + (n - 1) * 10) > d:
        return -1
    else:
        return (d - sum(l)) // 5


def snake_pattern(n, m):
    lines = []
    for i in range(n):
        lines.append(['#' * m,
                      '.' * (m - 1) + '#',
                      '#' * m,
                      '#' + '.' * (m - 1)][i % 4])
    return lines


def dungeon(a, b, c):
    s = a + b + c
    k = s // 9
    if s % 9 == 0 and a >= k and b >= k and c >= k:
        return "YES"
    else:
        return "NO"


def find_the_array(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            even += arr[i]
        else:
            odd += arr[i]
    res = arr[:]
    if even < odd:
        for i in range(len(res)):
            if i % 2 == 0:
                res[i] = 1
    else:
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = 1
    return res


def iq_test(nums):
    even = 0
    odd = 0
    pos_even = 0
    pos_odd = 0
    for i, v in enumerate(nums):
        if v % 2 == 0:
            even += 1
            pos_even = i + 1
        else:
            odd += 1
            pos_odd = i + 1
    return pos_even if even == 1 else pos_odd


def choosing_teams(k, arr):
    counter = 0
    for v in arr:
        if (5 - v) >= k:
            counter += 1
    return counter // 3


def eat_or_not(r, c, grid):
    a = set()
    b = set()
    for i in range(r):
        d = grid[i]
        for j, ch in enumerate(d):
            if ch == 'S':
                a.add(j)
                b.add(i)
    return r * c - len(a) * len(b)


def red_blue_shuffle(a, b):
    counter_a = 0
    counter_b = 0
    for ca, cb in zip(a, b):
        if ca > cb:
            counter_a += 1
        elif ca < cb:
            counter_b += 1
    if counter_a > counter_b:
        return "RED"
    elif counter_a < counter_b:
        return "BLUE"
    else:
        return "EQUAL"


def appleman_easy_task(strings):
    x = ''.join(strings)
    return "YES" if x == x[::-1] else "NO"


def bear_and_raspberry(c, l):
    ans = l[0] - l[1]
    for i in range(1, len(l) - 1):
        ans = max(ans, l[i] - l[i + 1])
    return max(0, ans - c)


def playing_with_dice(a, b):
    a_w = 0
    b_w = 0
    draw = 0
    for i in range(1, 7):
        if abs(i - a) < abs(i - b):
            a_w += 1
        elif abs(i - a) > abs(i - b):
            b_w += 1
        else:
            draw += 1
    return (a_w, draw, b_w)


def minimum_difficulty(l):
    n = len(l)
    x = max(l[i + 1] - l[i] for i in range(n - 1))
    y = min(l[i + 2] - l[i] for i in range(n - 2))
    return max(x, y)


def gregs_workout(arr):
    chest_count = sum(arr[0::3])
    biceps_count = sum(arr[1::3])
    back_count = sum(arr[2::3])
    ans = max(chest_count, biceps_count, back_count)
    if chest_count == ans:
        return "chest"
    elif biceps_count == ans:
        return "biceps"
    else:
        return "back"


def three_consecutive_even(l, r):
    if r - l + 1 < 3:
        return -1
    if l % 2 == 0:
        return (l, l + 1, l + 2)
    if r - l + 1 > 3:
        return (l + 1, l + 2, l + 3)
    return -1


def main(n: int):
    random.seed(0)

    # 1) Ilya and Bank Account
    x = random.randint(-10 * n, 10 * n)
    print("Ilya_and_Bank_Account input:", x, "output:", ilya_and_bank_account(x))

    # 2) Pashmak and Garden
    x1, y1 = random.randint(-n, n), random.randint(-n, n)
    x2, y2 = x1, y1 + random.randint(1, n)
    print("Pashmak_and_Garden input:", x1, y1, x2, y2, "output:", pashmak_and_garden(x1, y1, x2, y2))

    # 3) Dragons
    s = random.randint(1, 2 * n)
    pairs = [(random.randint(1, 2 * n), random.randint(0, 2 * n)) for _ in range(n)]
    print("Dragons:", dragons(s, pairs))

    # 4) Favorite Sequence
    arr = [random.randint(0, 1000) for _ in range(n)]
    print("Favorite_Sequence input:", arr, "output:", favorite_sequence(arr))

    # 5) Last Year's Substring
    s = ''.join(random.choice('2019') for _ in range(max(4, n)))
    print("Last_Years_Substring input:", s, "output:", last_years_substring(s))

    # 6) Devu and Churu Party
    d = 10 * n
    l = [random.randint(1, 10) for _ in range(n)]
    print("Devu_and_Churu input:", n, d, l, "output:", devu_and_churu_party(n, d, l))

    # 7) Snake pattern
    print("Snake_pattern:")
    for line in snake_pattern(n, max(2, n // 2)):
        print(line)

    # 8) Dungeon
    a = random.randint(0, 3 * n)
    b = random.randint(0, 3 * n)
    c = random.randint(0, 3 * n)
    print("Dungeon input:", a, b, c, "output:", dungeon(a, b, c))

    # 9) Find The Array
    arr2 = [random.randint(1, 100) for _ in range(n)]
    print("Find_The_Array input:", arr2, "output:", find_the_array(arr2))

    # 10) IQ test
    nums = [random.randint(1, 100) for _ in range(n)]
    print("IQ_test input:", nums, "output:", iq_test(nums))

    # 11) Choosing Teams
    arr3 = [random.randint(0, 5) for _ in range(n)]
    k = random.randint(1, 5)
    print("Choosing_Teams input:", k, arr3, "output:", choosing_teams(k, arr3))

    # 12) Eat or Not (cake)
    r = max(1, n // 2)
    c = max(1, n // 2)
    grid = []
    for _ in range(r):
        row = ''.join(random.choice('.S') for _ in range(c))
        grid.append(row)
    print("Eat_or_Not output:", eat_or_not(r, c, grid))

    # 13) Red-Blue Shuffle
    a_str = ''.join(random.choice('0123456789') for _ in range(n))
    b_str = ''.join(random.choice('0123456789') for _ in range(n))
    print("Red_Blue_Shuffle input:", a_str, b_str, "output:", red_blue_shuffle(a_str, b_str))

    # 14) Appleman and Easy Task
    strings = [''.join(random.choice('ab') for _ in range(n)) for _ in range(2)]
    print("Appleman_Easy_Task output:", appleman_easy_task(strings))

    # 15) Bear and Raspberry
    c_tax = random.randint(0, 10)
    prices = [random.randint(1, 100) for _ in range(n + 1)]
    print("Bear_and_Raspberry input:", c_tax, prices, "output:", bear_and_raspberry(c_tax, prices))

    # 16) Playing with Dice
    a_d = random.randint(1, 6)
    b_d = random.randint(1, 6)
    print("Playing_with_Dice input:", a_d, b_d, "output:", playing_with_dice(a_d, b_d))

    # 17) Minimum Difficulty
    if n < 3:
        seq = [random.randint(0, 100) for _ in range(3)]
    else:
        seq = [random.randint(0, 100) for _ in range(n)]
    print("Minimum_Difficulty input:", seq, "output:", minimum_difficulty(seq))

    # 18) Greg's Workout
    workout = [random.randint(1, 10) for _ in range(n)]
    print("Gregs_Workout input:", workout, "output:", gregs_workout(workout))

    # 19) Three consecutive with gcd 1 (original last code)
    l_val = random.randint(1, 2 * n)
    r_val = l_val + random.randint(0, 5)
    print("Three_consecutive_even input:", l_val, r_val, "output:", three_consecutive_even(l_val, r_val))


if __name__ == "__main__":
    main(10)