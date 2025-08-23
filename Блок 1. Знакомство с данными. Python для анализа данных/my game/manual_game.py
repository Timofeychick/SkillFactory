import numpy as np

random_number = np.random.randint(1, 101)  # загадываем число от 1 до 

count = 0

while True:
    count += 1
    user_number = int(input("Угадай число от 1 до 100: "))
    if user_number > random_number:
        print("Загаданное число меньше")
    elif user_number < random_number:
        print("Загаданное число больше")
    else:
        print(f"Вы угадали число! Это число = {random_number}, за {count} попыток")
        break  # конец игры, выход из цикла