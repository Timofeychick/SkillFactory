import numpy as np

def predict_number(number: int = 1) -> int:
    count = 0
    ref_value = 50
    step = 25   # начальный шаг

    while True:
        if number > ref_value:
            ref_value += step
        elif number < ref_value:
            ref_value -= step
        else:
            break  # угадали

        count += 1

        # уменьшаем шаг, но не даём ему стать меньше 1
        step = max(step // 2, 1)

    return count



def game_score(predict_number) -> int:
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
            
            
if __name__ == "__main__":
    # RUN
    game_score(predict_number)