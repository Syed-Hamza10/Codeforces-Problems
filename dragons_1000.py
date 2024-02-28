# Input
s, n = map(int, input().split())

dragons = []
for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

# Sort dragons based on their strength
dragons.sort()

# Iterate through each dragon
for dragon in dragons:
    x, y = dragon
    # If Kirito's strength is not greater than the dragon's strength, he loses the duel
    if s <= x:
        print("NO")
        break
    # If Kirito defeats the dragon, update his strength with the bonus
    s += y
else:
    print("YES")
