# Спроси слово, проверь — читается одинаково в обе стороны или нет. Выведи «да» или «нет».

n = input("Введи слово: ")
reverse = ""
for i in range(len(n)-1, -1, -1):
    reverse += n[i]
if n == reverse:
    print("Yes")
else:
    print("No") 

     