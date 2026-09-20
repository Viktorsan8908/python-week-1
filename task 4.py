# Спроси N, посчитай N! (1·2·3·...·N) циклом.

n = int(input("Введи число: "))
total = 1
for i in range(1, n + 1):
    total *= i
print(total)