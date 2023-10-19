string = input()

sorted = ''


help = [int(char) for char in string if char.isdigit()]
   

help.sort()

count = 0
for i in range(len(string)):
    if not string[i].isdigit():
        sorted += string[i]
    else:
        sorted += str(help[count])
        count += 1
          
print(sorted)          


