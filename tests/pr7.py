import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Подбросить кубик 2687 раз
n = 2687
rolls = np.random.randint(1, 7, size=n)

# 2. Определить частоты и частости
frequencies, counts = np.unique(rolls, return_counts=True)
relative_frequencies = counts / n

print("Значение:      ", frequencies)
print("Частоты:       ", counts)
print("Частости:      ", relative_frequencies)

# 3. Построить частотный вариационный ряд
freq_var_row = dict(zip(frequencies, counts))
print("Частотный вариационный ряд:", freq_var_row)

# 4. Построить гистограмму частот
plt.bar(frequencies, counts, width=0.6, color='b', alpha=0.7)
plt.xlabel('Значение на кубике')
plt.ylabel('Частота')
plt.title('Гистограмма частот')
plt.show()

# 5. Записать и построить эмпирическую функцию распределения
empirical_distribution = np.cumsum(relative_frequencies)
plt.step(frequencies, empirical_distribution, where='mid', label='Эмпирическая функция распределения')
plt.xlabel('Значение на кубике')
plt.ylabel('Кумулятивная частота')
plt.title('Эмпирическая функция распределения')
plt.legend()
plt.show()

# 6. Вычислить выборочное среднее, выборочную дисперсию и выборочное среднеквадратическое отклонение
sample_mean = np.mean(rolls)
sample_variance = np.var(rolls, ddof=0)
sample_std_dev = np.std(rolls, ddof=0)

print("Выборочное среднее:", sample_mean)
print("Выборочная дисперсия:", sample_variance)
print("Выборочное среднеквадратическое отклонение:", sample_std_dev)

# 7. Определить исправленную дисперсию и исправленное среднеквадратическое отклонение
corrected_variance = np.var(rolls, ddof=1)
corrected_std_dev = np.std(rolls, ddof=1)

print("Исправленная дисперсия:", corrected_variance)
print("Исправленное среднеквадратическое отклонение:", corrected_std_dev)

# 8. Найти моду и медиану
mode_result = stats.mode(rolls)
mode_value = mode_result.mode
median = np.median(rolls)

print("Мода:", mode_value)
print("Медиана:", median)

# 9. Найти коэффициент вариации
coefficient_of_variation = (sample_std_dev / sample_mean) * 100

print("Коэффициент вариации (%):", coefficient_of_variation)

# 10. Вычислить среднее линейное отклонение
mean_absolute_deviation = np.mean(np.abs(rolls - sample_mean))

print("Среднее линейное отклонение:", mean_absolute_deviation)

# 11. Найти асимметрию
skewness = stats.skew(rolls)

print("Асимметрия:", skewness)

# 12. Найти эксцесс
kurtosis = stats.kurtosis(rolls)

print("Эксцесс:", kurtosis)
