import pandas as pd
import numpy as np


chat_id = 5223715667 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    significance = 0.06
    stat, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt],  alternative='two-sided')
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return p_value < significance # Ваш ответ, True или False
