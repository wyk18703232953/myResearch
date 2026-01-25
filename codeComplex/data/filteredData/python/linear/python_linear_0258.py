def palindrome(s):
    i = 0
    j = len(s) - 1
    p = True
    while i <= j:
        if s[i] != s[j]:
            p = False
            break
        i += 1
        j -= 1
    return p

def core_logic(s):
    ans = 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            if not palindrome(s[i:j + 1]):
                ans = max(ans, len(s[i:j + 1]))
                break
    return ans

def build_input_string(n):
    if n <= 0:
        return ""
    chars = ['a', 'b', 'c', 'd']
    s_list = [chars[i % len(chars)] for i in range(n)]
    return "".join(s_list)

def main(n):
    s = build_input_string(n)
    result = core_logic(s)
    print(result)

if __name__ == "__main__":
    main(10)