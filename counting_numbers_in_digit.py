def foo(digit):
    count = 0
    while digit > 0:
        digit = int(digit / 10)
        count += 1
    return count
print(foo(123456789))
   