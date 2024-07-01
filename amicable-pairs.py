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
amicable_numbers = []
    
for num in range(start, end + 1):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
        
    second_sum = 0
    for i in range(1, sum):
        if sum % i == 0:
            second_sum += i

    if sum > num and second_sum == num:
        amicable_numbers.append((num, sum))

print()
print(*amicable_numbers)