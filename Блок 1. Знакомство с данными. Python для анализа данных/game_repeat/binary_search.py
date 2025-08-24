import numpy as np

random_number = np.random.randint(1, 101)  # загадали число от 1 до 100

def bin_search(num: int = 1) -> int:

    count = 0
    ref_value = 50
    step = 25
    
    while True:
        
        if num > ref_value:
            ref_value += step
        elif num < ref_value:
            ref_value -= step
        else:
            break  # угадали
        
        count += 1
        step = max(step // 2, 1)
        
    # print(f"Вы угадали число {num} за {count} попыток!")
    return count

# bin_search(random_number)

def mean_game_score(func) -> int:
    
    counts = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        counts.append(func(number))
        
    score = int(np.mean(counts))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

mean_game_score(bin_search)