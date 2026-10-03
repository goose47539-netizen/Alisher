print("Начало")

print("Проснуться")
print("Собрать рюкзак")

while True:
    answer = input("Всё положил? (да/нет): ")

    if answer == "да":
        break
    else:
        print("Положить нужные вещи")

rain = input("Идёт дождь? (да/нет): ")

if rain == "да":
    print("Взять зонт")
else:
    print("Зонт не брать")

print("Идти в колледж")
print("Конец")