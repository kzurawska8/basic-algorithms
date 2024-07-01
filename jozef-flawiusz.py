quantity = int(input("Podaj liczbę żołnierzy: "))
safe_place = []

soldiers = list(range(1, quantity + 1))
idx = 0

while len(soldiers) > 1:
        m = 2
        idx = (idx + m - 1) % len(soldiers)
        soldiers.pop(idx)

safe_place.append(soldiers[0])

print()
print(*safe_place)