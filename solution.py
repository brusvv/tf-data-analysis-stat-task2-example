import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import t

chat_id = 5437824033

def solution(p: float, x: np.array) -> tuple:
    alpha = p
    measurements = x
    n = measurements.size
    x_mean = np.mean(measurements)
    s = np.sqrt(np.var(measurements, ddof=1))
    t_alpha_2 = t.ppf(1 - alpha/2, df=n-1)
    delta = t_alpha_2 * s / np.sqrt(n)
    left_boundary = x_mean - delta
    right_boundary = x_mean + delta
    return (left_boundary, right_boundary)
