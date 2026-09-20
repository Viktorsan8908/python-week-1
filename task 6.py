n = input("Введи солово: ")
vowels = "аеёиоуыэюя"
count = 0
for i in n:
    if i in vowels:
        count += 1
print(count)
