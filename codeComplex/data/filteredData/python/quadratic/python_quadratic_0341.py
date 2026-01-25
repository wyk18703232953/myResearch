import sys
import math
from collections import defaultdict, deque

def main(n):
    # n is the length of the strings
    if n <= 0:
        print(-1)
        return

    # Deterministic construction of s and t based on n
    # s: 'a', 'b', 'c', ... cyclic
    # t: rotated version of s by 1 position to ensure they are anagrams
    alphabet = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = alphabet[:]  # original order
    t = alphabet[1:] + alphabet[:1]  # rotation by 1

    res = True
    ans = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        else:
            ind = -1
            for j in range(i + 1, n):
                if t[i] == s[j]:
                    ind = j
                    break
            if ind == -1:
                res = False
                break
            for j in range(ind - 1, i - 1, -1):
                ans.append(j + 1)
                s[j], s[j + 1] = s[j + 1], s[j]
    if res:
        print(len(ans))
        if ans:
            print(*ans)
    else:
        print(-1)

if __name__ == "__main__":
    main(10)