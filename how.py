score = int(input("Введите балл: "))

if score < 0 or score > 100:
    print("Ошибка ввода")
elif score >= 90:
    print(5)
elif score >= 75:
    print(4)
elif score >= 60:
    print(3)
else:
    print(2)