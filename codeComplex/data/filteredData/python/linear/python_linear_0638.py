from __future__ import division

def solve(a):
    n = len(a)
    cap = [0] + a[:]

    ones = []
    others = []

    for i in range(n):
        if a[i] == 1:
            ones.append(i + 1)

        else:
            others.append(i + 1)

    outputs = []

    def write(x):
        outputs.append(str(x))

    if len(others) == 0:
        if len(ones) == 1:
            write("YES 0")
            write("0")

        else:
            write("NO")
        return "\n".join(outputs)

    dia = len(others)
    graph = []

    for j in range(len(others) - 1):
        graph.append((others[j], others[j + 1]))
        cap[others[j]] -= 1
        cap[others[j + 1]] -= 1

    if len(ones) > 0:
        this = ones.pop()
        graph.append((this, others[0]))
        cap[others[0]] -= 1
        dia += 1

    if len(ones) > 0:
        this = ones.pop()
        graph.append((this, others[-1]))
        cap[others[-1]] -= 1
        dia += 1

    done = False
    for j in range(len(others)):
        while cap[others[j]] > 0:
            if len(ones) > 0:
                this = ones.pop()
                graph.append((this, others[j]))
                cap[others[j]] -= 1

            else:
                done = True
                break
        if done:
            break

    if len(ones) > 0:
        write("NO")

    else:
        write("YES " + str(dia - 1))
        write(len(graph))
        for x, y in graph:
            write(str(x) + " " + str(y))

    return "\n".join(outputs)


def main(n):
    if n <= 0:
        return ""

    # Deterministic generation of capacities:
    # Alternate between 1 and values >= 2 so that structure scales with n
    a = [(i % 3) + 1 for i in range(n)]
    return solve(a)


if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    result = main(10)
    if result:
        # print(result)
        pass