import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
  t = 56
  n = len(x)
  mu = 0
  sigma = 1

  x_error = np.random.normal(mu, sigma, n)
  a = 2 * x_error/ t**2

  return a.mean()
