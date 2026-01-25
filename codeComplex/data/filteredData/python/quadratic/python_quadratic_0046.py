import sys

def main(n):
    m = 10**9 + 7
    # generate deterministic command sequence of length n-1 using 'f' and 's'
    # pattern: repeat ['f', 's', 's'] to cover n-1 positions
    pattern = ['f', 's', 's']
    cmds = [pattern[i % 3] for i in range(max(0, n-1))]

    curr = [0] * (n + 20)
    last = [0] * (n + 20)
    curr[0] = 1

    for s_idx in range(1, n):
        last, curr = curr, last
        if cmds[s_idx - 1] == 'f':
            curr[0] = 0
            for i in range(len(last) - 1):
                curr[i + 1] = last[i]
        else:  # 's'
            curr[-1] = 0
            for i in range(len(last) - 2, -1, -1):
                curr[i] = (curr[i + 1] + last[i]) % m

    s_val = 0
    for x in curr:
        s_val = (s_val + x) % m
    print(s_val)


if __name__ == "__main__":
    # example deterministic call; adjust n for experiments
    main(1000)