"""
https://codeforces.com/contest/608/problem/B
01
00111 should output 3

0011
0110 should output 2
"""
first = [int(i) for i in input()]
second = [int(i) for i in input()]

pref_dists = [
    [0] + [int(0 != c) for c in second],
    [0] + [int(1 != c) for c in second]
]
for i in range(1, len(second) + 1):
    pref_dists[0][i] += pref_dists[0][i - 1]
    pref_dists[1][i] += pref_dists[1][i - 1]

total = 0
for i, c in enumerate(first):
    end = len(second) - (len(first) - i)
    total += pref_dists[c][end + 1] - pref_dists[c][i]
print(total)
