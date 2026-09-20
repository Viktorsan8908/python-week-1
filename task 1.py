# Спроси N, посчитай сумму 1+2+...+N циклом.
n = int(input("Введи число: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)