from functools import cache

@cache
def fibbonachi(n):
    if n<= 1:
        return 1
    return fibbonachi(n-1) + fibbonachi(n-2)

print(fibbonachi(450))