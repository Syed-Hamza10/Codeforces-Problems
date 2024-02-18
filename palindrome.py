def is_palindrome(n):
    n = str(n)
    rev = n[::-1]
    return 'true' if n == rev else 'false'
print(is_palindrome('level'))