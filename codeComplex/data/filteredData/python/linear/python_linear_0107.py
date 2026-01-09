def main(n):
    # Deterministically generate two strings based on n
    # str1 length = n, str2 length = 1 (since original code only uses first char of str2)
    if n <= 0:
        str1 = ""

    else:
        # Generate a pattern of lowercase letters: 'a'..'z' cycling
        str1 = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    # str2 single character depends on n deterministically
    # Map n to a lowercase letter
    ch2 = chr(ord('a') + (n % 26))
    str2 = ch2

    lst = []
    lst_ans = []
    l_count = 0
    count = 0

    for i in str2:
        if count < 1:
            lst.append(i)

        else:
            break

    for i in str1:
        if count == 0:
            lst_ans.append(i)
            count += 1
        elif ord(i) < ord(lst[0]):
            lst_ans.append(i)

        else:
            lst_ans.append(lst[0])
            break

    else:
        lst_ans.append(lst[0])

    # Return the result string instead of printing, to make it reusable in experiments
    return ''.join(lst_ans)


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for n in [1, 5, 10, 20]:
        result = main(n)
        # print(f"n={n}, result={result}")
        pass