def main(n):
    # Interpret n as the size of the list E
    if n < 3:
        # Not enough elements to form (i, j, k) with i < j < k
        # print(-1)
        pass
        return

    # Deterministically generate U and E based on n
    # U grows with n so that some (Ek - Ei) <= U pairs exist
    U = n // 2 + 1
    # Strictly increasing sequence to keep Ek - Ei > 0
    E = [i * 2 for i in range(n)]

    ind_i = 0
    prev_ind_k = ind_i + 2

    maxi_efficiency = -1
    turn = 0
    for ind_i in range(0, n - 2):
        ind_j = ind_i + 1
        prev_ind_k = max(prev_ind_k, ind_i + 2)
        Ei = E[ind_i]
        Ej = E[ind_j]
        for ind_k in range(prev_ind_k, n + 1):
            if ind_k == n:
                prev_ind_k = n - 1
                break
            Ek = E[ind_k]
            if (Ek - Ei) > U:
                prev_ind_k = ind_k - 1
                break

            efficiency = (Ek - Ej) / (Ek - Ei)
            if efficiency > maxi_efficiency:
                maxi_efficiency = efficiency

    # print(maxi_efficiency)
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)