from collections import deque

def main(n):
    # Generate deterministic input data based on n
    # orderedli: a permutation-like sequence of length n
    orderedli = [(i * 2 + 3) % (n + 7) + 1 for i in range(n)]
    # Ensure uniqueness for mapping by simple adjustment if collisions occur
    seen = {}
    unique_orderedli = []
    offset = n + 10
    for x in orderedli:
        if x in seen:
            x += offset
            offset += 1
        seen[x] = True
        unique_orderedli.append(x)
    orderedli = unique_orderedli

    # s: a binary string of length 2n with exactly n zeros and n ones
    # pattern: first n zeros then n ones to exercise stack behavior
    s = "0" * n + "1" * n

    indexof = {}
    for i, x in enumerate(orderedli):
        indexof[x] = i + 1

    sortedli = list(sorted(orderedli))
    i = 0

    st = deque()
    outputs = []

    for x in s:
        if x == "0":
            st.append(sortedli[i])
            outputs.append(str(indexof[sortedli[i]]))
            i += 1

        else:
            temp = st.pop()
            outputs.append(str(indexof[temp]))

    # print(" ".join(outputs))
    pass
if __name__ == "__main__":
    main(5)