import random

for game in range(1, 4):
    secret = random.randint(1, 8)
    attempts = 0

    low = 1
    high = 8

    print("Игра", game)

    while True:
        print("Диапазон:", low, "-", high)

        guess = int(input("Твоя догадка: "))
        attempts += 1

        if guess == secret:
            print("Угадал!")
            print("Попыток:", attempts)
            break

        elif guess < secret:
            print("Загаданное число больше")
            low = guess + 1

        else:
            print("Загаданное число меньше")
            high = guess - 1

    print()