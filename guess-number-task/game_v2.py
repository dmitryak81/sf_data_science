"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

# Минимальное и максимальное значения, которое может принимать угадываемое число
const_min_value = 1; const_max_value = 100


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    global const_min_value, const_max_value
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(const_min_value, const_max_value+1)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def smart_predict(number: int = 1) -> int:
    """Рандомно угадываем число в заданном диапазоне, но дополнительно используем 
    информацию о том, больше или меньше случайное число, чем загаданное

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """    
    global const_min_value, const_max_value
    
    count = 0
    
    # Инициализируем границы диапазона, в котором находится угадываемое число
    left = const_min_value
    right = const_max_value+1
    while True:
        count += 1
        predict_number = np.random.randint(left, right)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        
        # загаданное число меньше, нашего варианта, мы можем сдвинуть правую границу
        # получим новый интервал для угадывания [left, predict_number)
        if number < predict_number:
            right = predict_number
        else: # иначе двигаем левую границу --> интервал: [predict_number+1, right]
            left = predict_number+1
    return count
    

def score_game(predict_func, show_statistic: bool = False) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_func ([type]): функция угадывания
        show_statistic: если True, выводит на экран минимальное и максимальное количество попыток. Defalts to False

    Returns:
        int: среднее количество попыток
    """
    global const_min_value, const_max_value
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(const_min_value, const_max_value+1, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))        
    if (show_statistic):
        print('Min:', int(np.min(count_ls)))
        print('Max:', int(np.max(count_ls)))
        print('Median:', int(np.median(count_ls)))
        print(f'Mean: {score}')
    return score


if __name__ == "__main__":
    # RUN
    score = score_game(random_predict, True)
    print(f"Решение 'в лоб' угадывает число в среднем за: {score} попыток")
    
    score = score_game(smart_predict, True)
    print(f"Умный алгоритм угадывает число в среднем за: {score} попыток")
    
