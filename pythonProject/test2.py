import numpy as np
from scipy.stats import t
import pprint

# Данные
X = [0, 0, -9, 17, -2, -8, -10, -10, -9, -7, 14, 10, 5, 9, 14, 1, 0, 13, 4, 0, -6, 20, 11, 1, 18, -6, 7, 13, 20, 14, 17, 15, -6, 12, -2, 16, -9, 1, 3, -2, 15, 11, 15, -5, 9, 14, 15, 7, 5, 1, 4, -8, 3, -2, 15, -7, -5, -4, -2, -9, 18, -6, -8, -10, 14, 0, -4, 10, 7, -1, 17, -9, -10, -9, 16, 10, 3, 2, -5, 2, -1, 15, -9, 12, 3, 16, -5, 9, 13, 5, -2, 14, 10, 11, 18, 12, -8, -3, 19]
Y = [0, 11, 16, 16, 2, 6, -26, 9, 21, 5, 16, 6, 5, 30, 4, 7, 22, 2, 13, 0, 16, 21, 25, 22, 0, 19, 19, 7, 0, 23, 6, 20, 28, 21, 8, 4, 15, 30, 7, 25, 17, 14, 26, 14, 8, 16, 8, 18, 15, 5, 8, 28, 4, 27, 29, 29, 21, 7, 23, 29, 0, 1, 7, 14, 4, 23, 26, 19, 27, 23, 14, 16, 8, 0, 4, 16, 10, 0, 24, 3, 10, 6, 1, 20, 26, 4, 24, 11, 30, 14, 10, 26, 12, 20, 10, 14, 18, 27, 13]

# Определение сумм
sum_x = np.sum(X)
sum_y = np.sum(Y)

# Определение сумм квадратов
sum_x2 = np.sum(np.square(X))
sum_y2 = np.sum(np.square(Y))

# Сумма произведений xy
sum_xy = np.sum(np.multiply(X, Y))

# Средние значения
mean_x = np.mean(X)
mean_y = np.mean(Y)
mean_xy = np.mean(np.multiply(X, Y))

# Дисперсии
var_x = np.var(X, ddof=1)
var_y = np.var(Y, ddof=1)

# Среднеквадратические отклонения
std_x = np.std(X, ddof=1)
std_y = np.std(Y, ddof=1)

# Ковариация
cov_xy = np.cov(X, Y)[0, 1]

# Линейный коэффициент корреляции
corr_xy = np.corrcoef(X, Y)[0, 1]

# Доверительный интервал для коэффициента корреляции
n = len(X)
alpha = 0.05
t_crit = t.ppf(1 - alpha/2, n - 2)
se_corr = np.sqrt((1 - corr_xy**2) / (n - 2))
conf_interval = (corr_xy - t_crit * se_corr, corr_xy + t_crit * se_corr)

# Наблюдаемое значение критерия Стъюдента
t_observed = corr_xy * np.sqrt((n - 2) / (1 - corr_xy**2))

# Нулевую гипотезу проверяем о том, что корреляция равна нулю (т.е. нет линейной связи)
# Найдем теоретическое значение критерия Стъюдента для уровня значимости alpha и степени свободы n - 2
t_theoretical = t.ppf(1 - alpha/2, n - 2)

# Результаты
results = {
    'sum_x': sum_x,
    'sum_y': sum_y,
    'sum_x2': sum_x2,
    'sum_y2': sum_y2,
    'sum_xy': sum_xy,
    'mean_x': mean_x,
    'mean_y': mean_y,
    'mean_xy': mean_xy,
    'var_x': var_x,
    'var_y': var_y,
    'std_x': std_x,
    'std_y': std_y,
    'cov_xy': cov_xy,
    'corr_xy': corr_xy,
    'conf_interval': conf_interval,
    't_observed': t_observed,
    't_theoretical': t_theoretical,
    'reject_null_hypothesis': abs(t_observed) > t_theoretical
}

pprint.pprint(results)