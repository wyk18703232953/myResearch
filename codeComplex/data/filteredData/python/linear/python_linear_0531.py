import string


def main(n):
    # Interpret n as k (number of letters to consider from uppercase)
    # Ensure k is between 1 and 26
    k = max(1, min(26, n))

    # Deterministically generate a string consisting of uppercase letters A-Z
    # Length of the string grows with n to scale the experiment
    length = max(1, n * 10)
    s = ''.join(string.ascii_uppercase[i % 26] for i in range(length))

    mp = {}
    for ch in string.ascii_uppercase[:k]:
        mp[ch] = 0
    for ch in s:
        if ch in mp:
            mp[ch] += 1
    result = min(mp.values()) * k
    # print(result)
    pass
if __name__ == "__main__":
    main(10)