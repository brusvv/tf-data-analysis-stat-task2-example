import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import laplace

chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = np.median(x)
    temp = np.zeros(len(x))
    for i in range(len(x)):
        temp[i] = x[i] - loc
    #D = 2*(np.sum(temp))**2
    #D = D/len(x)
    #D = D/len(x)
    #scale = np.sqrt(D) / np.sqrt(len(x))
    scale = np.sqrt(2)*np.sum(temp) / np.sqrt(len(x))
    return (2 / 56**2)*loc - (2 / 56**2)*scale * laplace.ppf(1 - alpha / 2), \
           (2 / 56**2)*loc - (2 / 56**2)*scale * laplace.ppf(alpha / 2)
