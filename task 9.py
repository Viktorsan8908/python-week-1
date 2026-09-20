secret = 7

while True:
    num = int(input("Отгадай число: "))
    if secret > num:
        print("Меньше")
    elif secret < num:
        print("Больше")
    else:
        print("Молодец")
        break