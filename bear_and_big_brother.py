n,m = map(int ,input().split())


years = 0

while n <= m:
    n *= 3
    m *= 2
    years+=1
print(years)    


