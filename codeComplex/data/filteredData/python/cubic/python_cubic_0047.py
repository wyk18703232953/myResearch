def main(n):
    # Generate a deterministic input string of length n
    # Pattern: lowercase letters repeating 'a' to 'z'
    s = [chr(ord('a') + (i % 26)) for i in range(n)]

    dic = {}
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            ele = "".join(s[i:j+1])
            if ele not in dic:
                dic[ele] = 1

            else:
                dic[ele] += 1

    ans = []
    for key in dic.keys():
        if dic[key] >= 2:
            ans.append(len(key))
    ans.sort()
    if ans == []:
        # print(0)
        pass

    else:
        # print(ans[-1])
        pass
if __name__ == "__main__":
    main(10)