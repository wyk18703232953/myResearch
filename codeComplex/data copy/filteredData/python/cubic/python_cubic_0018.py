def main(n):
    # Generate a deterministic string of length n
    # Use lowercase letters repeated in a pattern
    letters = [chr(ord('a') + (i % 26)) for i in range(n)]
    string = "".join(letters)

    length = len(string)
    li = []
    match_li = []

    for i in range(length):
        letter = string[i]
        letters_sub = letter
        if letter in li:
            match_li.append(letter)
        li.append(letter)
        for j in range(i + 1, length):
            letters_sub += string[j]
            if letters_sub in li:
                match_li.append(letters_sub)
            li.append(letters_sub)

    longest = 0
    for k in match_li:
        if len(k) > longest:
            longest = len(k)

    # print(longest)
    pass
if __name__ == "__main__":
    # Example call for experimental purposes
    main(10)