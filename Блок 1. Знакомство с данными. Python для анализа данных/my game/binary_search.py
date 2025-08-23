import numpy as np

def predict_number_2(number) -> int:
    count = 1
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
        print(f'текущее значение {ref_value}, попытка {count}, число {number}')

        # уменьшаем шаг, но не даём ему стать меньше 1
        step = max(step // 2, 1)

    return print(f'угадали число {number}, за {count} попыток')