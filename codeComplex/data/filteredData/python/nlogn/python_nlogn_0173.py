def main(n):
    length = n
    start = []
    end = []
    for i in range(length):
        # Deterministically generate a and b based on i and n
        a = i + 2
        b = (i * 3 + n) % (i + 2)
        e, s = a - b, a + b
        end.append([e, i])
        start.append([s, i])

    end.sort(key=lambda x: x[0])
    start.sort(key=lambda x: x[0])

    cant_visit = set()
    answer = 0
    end_index = 0
    for s, i in start:
        if i not in cant_visit:
            answer += 1
            while end_index < length and end[end_index][0] < s:
                cant_visit.add(end[end_index][1])
                end_index += 1

    print(answer)


if __name__ == "__main__":
    main(10)