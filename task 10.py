n = int(input("Введи число: "))
total = 0
while n != 0:
    
    total += n % 10
    n //= 10
print(total)