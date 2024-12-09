from interval_series import *
from latex_generator import dict_to_latex_table_str, get_latex_form_empirical_distribution_func
from prob_plotting import *
from sample_functions import *


# nums = [-0.45, 1.42, 0.52, 0.66, -1.63, -1.70, -0.42,
#         0.17, -1.18, 0.14, 1.62, -1.71, 0.43, -0.18,
#         1.42, 0.69, -0.55, -0.70, -1.51, -0.68]
# nums = [0.83, 0.73, -0.48, 0.00, -1.35, 1.59, 0.31, 0.17,
#         0.59, -0.45, -0.03, 0.73, -0.59, -1.59, 0.38, 1.49, 0.14, -0.62, -1.59, 1.45]

nums = [-0.03, -0.59, 0.38, 0.73, -1.59, 1.49, 0.14, -1.59, -0.38, -0.62, 1.45, -1.49, -0.15, 0.06, 0.61, -0.05, 0.63, -1.59, 0.62, 1.56]
# Необходимо определить следующие статистические
# характеристики: вариационный ряд, экстремальные значения и размах,
# оценки математического ожидания и среднеквадратического отклонения,
# эмпирическую функцию распределения и её график, гистограмму и
# полигон приведенных частот группированной выборки.

### вариационный ряд, экстремальные значения и размах
print("Выборочный ряд:", get_variation_series_pretty(nums))
print(get_extremes(nums))
print("Размах: {:.2f}".format(get_whole_range(nums)))
print(f"Мода: {get_mode(nums)}")

### оценки математического ожидания и среднеквадратического отклонения
expected_value = get_expected_value_estimate(nums)

print("Оценка математического ожидания: {:.2f}"
    .format(expected_value))
print("Стандартное отклонение {:.2f}"
    .format(get_expected_value_deviation(nums)))
print("Оценка выборочного среднеквадратического отклонения: {:.4f}"
    .format(get_sample_standard_deviation(nums, expected_value)))
print("Оценка выборочного с.к.о. (исправленная): {:.4f}"
    .format(get_sample_standard_deviation_corrected(nums, expected_value)))

### эмпирическая функция распределения и её график
plot_function(nums, lambda x: empirical_distribution_function(x, nums))

### гистограмма и полигон приведенных частот группированной выборки
plot_histogram(nums)

### Помощь для теха
path_to_analytical_func_tex = "output/analytical_func.tex"
with open(path_to_analytical_func_tex, "w") as f:
    f.write(get_latex_form_empirical_distribution_func(nums,
        lambda x: empirical_distribution_function(x, nums)))
print(f"Вид эмпирической функции распределения: записан в {path_to_analytical_func_tex}")

path_to_statistical_interval_series_tex = "output/statistical_series.tex"
with open("output/statistical_interval_series.tex", "w") as f:
    output = dict_to_latex_table_str(get_statistical_interval_series(nums))
    f.write(output)
print(f"Интервальный ряд: записаны в {path_to_statistical_interval_series_tex}")

path_to_statistical_series = "output/statistical_series.tex"
with open(path_to_statistical_series, "w") as f:
    output = dict_to_latex_table_str(get_statistical_series(nums))
    f.write(output)
print(f"Статистический ряд: записаны в {path_to_statistical_series}")
