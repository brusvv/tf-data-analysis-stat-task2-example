import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    a = 0.005
    alpha = 1 - p
    lower_bound = uniform.ppf(alpha / 2, loc=a, scale=(np.max(x) - a) / n)
    upper_bound = uniform.ppf(1 - alpha / 2, loc=a, scale=(np.max(x) - a) / n)
    return (lower_bound, upper_bound)
