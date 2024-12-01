def find_best_arrangement(case):
    S1, F1, H1, S2, F2, H2, S3, F3, H3 = case

    total_s = S1 + S2 + S3
    total_f = F1 + F2 + F3
    total_h = H1 + H2 + H3

    costs = []

    costs.append(("SFH", (total_s - S1) + (total_f - F2) + (total_h - H3)))
    costs.append(("SHF", (total_s - S1) + (total_h - H2) + (total_f - F3)))
    costs.append(("FSH", (total_f - F1) + (total_s - S2) + (total_h - H3)))
    costs.append(("FHS", (total_f - F1) + (total_h - H2) + (total_s - S3)))
    costs.append(("HSF", (total_h - H1) + (total_s - S2) + (total_f - F3)))
    costs.append(("HFS", (total_h - H1) + (total_f - F2) + (total_s - S3)))

    best_arrangement = min(costs, key=lambda x: (x[1], x[0]))
    return best_arrangement


if __name__ == '__main__':
    t = int(input())
    results = []
    for _ in range(t):
        case = list(map(int, input().split()))
        arrangement, moves = find_best_arrangement(case)
        results.append(f"{arrangement} {moves}")
    print("\n".join(results))
