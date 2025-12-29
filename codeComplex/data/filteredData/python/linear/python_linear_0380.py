from collections import Counter
import random
import string

def solve_one(s: str) -> str:
    d = Counter(s)
    if '1' in d:
        news = ""
        for ch in s:
            if ch != '1':
                news += ch
        ind = len(news)
        for i in range(len(news)):
            if news[i] == '2':
                ind = i
                break
        return news[0:ind] + '1' * d['1'] + news[ind:]
    else:
        return s

def generate_test_string(n: int) -> str:
    # Generate a random string of length n using digits 0-3
    # (contains '1', '2' often enough for testing)
    alphabet = "0123"
    return ''.join(random.choice(alphabet) for _ in range(n))

def main(n: int):
    """
    n: scale parameter, used here as the length of the generated test string.
    Prints the processed string.
    """
    s = generate_test_string(n)
    ans = solve_one(s)
    print(ans)

if __name__ == "__main__":
    # Example: run with n = 20
    main(20)