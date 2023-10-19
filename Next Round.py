n, k = map(int, input().split())
count = 0
a = list(map(int, input().split()))

k_position = a[k-1]

for i in a:
    if i >=k_position and i>0:
        count+=1
print(count)