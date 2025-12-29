import random
import string


def generate_tile():
    # digits 1-9 and suits m,p,s (as in typical mahjong problems)
    d = random.randint(1, 9)
    s = random.choice(['m', 'p', 's'])
    return f"{d}{s}"


def main(n: int):
    # n controls how many random test triples we generate
    # For each triple, compute and print the answer as in the original code
    for _ in range(n):
        t1 = generate_tile()
        t2 = generate_tile()
        t3 = generate_tile()

        ans = 2
        if t1 == t2 or t2 == t3 or t3 == t1:
            if t1 == t2 == t3:
                ans = 0
            else:
                ans = 1

        aaa = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if k - j == j - i == 1:
                        aaa.append({i, j, k})

        if (
            t1[1] == t2[1] == t3[1]
            and {int(t1[0]), int(t2[0]), int(t3[0])} in aaa
        ):
            ans = 0
        elif (
            t1[1] == t2[1]
            and (abs(int(t1[0]) - int(t2[0])) in (1, 2))
        ) or (
            t1[1] == t3[1]
            and (abs(int(t1[0]) - int(t3[0])) in (1, 2))
        ) or (
            t3[1] == t2[1]
            and (abs(int(t3[0]) - int(t2[0])) in (1, 2))
        ):
            ans = min(1, ans)

        # Output one line per test triple: the tiles and the computed answer
        print(t1, t2, t3, ans)


if __name__ == "__main__":
    # example run: generate 5 random test triples
    main(5)