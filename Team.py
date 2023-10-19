n = int(input())
solved = 0

for i in range(n):
    opinion = input()
    opinion = opinion.split()
    print(opinion)
    for i in range(len(opinion)):
        opinion[i] = int(opinion[i])                
    if sum(opinion) >= 2:
        solved += 1

print(solved)