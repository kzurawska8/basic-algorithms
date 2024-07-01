def get_valid_range():
    while True:
        try:
            option = input("Podaj zakres (x, y): ")
            scope = option.split(", ")

            if len(scope) != 2:
                raise ValueError("\nPodaj dokładnie dwie liczby oddzielone przecinkiem.")

            start = int(scope[0])
            end = int(scope[1])

            if start > end:
                raise ValueError("\nPoczątek zakresu nie może być większy od końca zakresu.")

            return start, end
        
        except ValueError as e:
            print(f"\nBłąd: {e}\n")

start, end = get_valid_range()
result = []

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)

print()
print(result)