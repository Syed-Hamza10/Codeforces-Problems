n, k = map(int,input().split())

# numbers = []
# for i in range(1,n+1):
#     if i%2 == 1:
#         numbers.append(i)

# for i in range(1,n+1):
#     if i%2 == 0:
#         numbers.append(i)

# print(numbers)

import math as m
def foo(n, k):
    if k < m.ceil(n/2):
        return (2*(k-1)) + 1
    else:
        k -= m.ceil(n/2)
        return 2*k
print(foo(10,3))

# [1,3,5,7,9,2,4,6,8,10]
# [1,3,5,7,2,4,6]