import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import uniform


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = loc / pow(p, len(x))
    return loc * uniform.ppf(1 - alpha / 2), \
           scale * uniform.ppf(alpha / 2)
