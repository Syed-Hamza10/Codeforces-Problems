def foo(digit):
    reverse_number = 0
    while digit > 0:
        last_digit = digit % 10
        digit = int(digit/10)
        reverse_number = (reverse_number*10) + last_digit
    return reverse_number   
        
print(foo(123456789))

def alternate_method(n):
    n = str(n)
    rev = n[::-1]
    return int(rev)
print(alternate_method(0))