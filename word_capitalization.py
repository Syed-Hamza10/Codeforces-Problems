string = input()
upper = ''

for char in string:
    if ord(char) >=97 and ord(char) <= 123:
        char = ord(char) - 32
        upper += chr(char)
    else:
        upper += char    
    break
count = 0    
for char in string:
    if count != 0:
        upper += char
    count+=1    
    

print(upper)
