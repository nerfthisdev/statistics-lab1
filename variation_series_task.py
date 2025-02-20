### вариационный ряд, экстремальные значения и размах
# from interval_series import *
from latex_generator import *
from nums import get_first_task_nums
from prob_plotting import plot_function, plot_polygon
from variation_series import *

# Лабораторная работа № 1 (расчётная часть)
# 1. Для выборки А:
# - указать максимальный и минимальный элементы выборки, найти размах выборки;
# - построить статистический ряд и начертить полигон ряда;
# - записать эмпирическую функцию распределения и построить её график;
# - вычислить начальные и центральные эмпирические моменты до 4-го порядка;
# - найти моду, медиану, коэффициенты асимметрии (момент 3-его порядка) и эксцесса (sum_{i=1}^{k} x_i - x_{ср})/(n*\sigma) - 3 не забыть минус три;
# - сделать выводы и сформулировать гипотезы о распределении генеральной совокупности из которой извлечена выборка, оценить параметры этого распределения

ACCURACY = 4
nums = get_first_task_nums()

print("Вариационный ряд:", get_variation_series_pretty(nums))
print(get_extremes(nums))
print("Размах: {:.2f}".format(get_whole_range(nums)))

statistical_series = get_statistical_series(nums)
path_to_statistical_series = "tex/output/task1/statistical_series.tex"
with open(path_to_statistical_series, "w") as f:
    output = dict_to_latex_table_str(statistical_series)
    f.write(output)
print(f"Статистический ряд: записаны в {path_to_statistical_series}")

plot_polygon(statistical_series.keys(), statistical_series.values(), "tex/output/task1/polygon.png")

### оценки математического ожидания и среднеквадратического отклонения
expected_value = get_expected_value_estimate(nums)
confidence_prob = 0.9

print(
    "Оценка математического ожидания (начальный момент): "
    + str(round(expected_value, ACCURACY))
)

print(
    "Стандартное отклонение" + str(round(get_expected_value_deviation(nums), ACCURACY))
)
print("Дисперсия " + str(round(get_sample_variance(nums, expected_value), ACCURACY)))

print(
    "Оценка выборочного среднеквадратического отклонения: "
    + str(round(get_sample_standard_deviation(nums, expected_value), ACCURACY))
)

print(
    "Оценка выборочного с.к.о. (исправленная): "
    + str(
        round(get_sample_standard_deviation_corrected(nums, expected_value), ACCURACY)
    )
)
# print(
#     f"Доверительный интервал с.к.о.с доверительной вероятностью ɣ=\n{confidence_prob}",
#     get_confidence_interval_for_standard_deviation(
#         get_sample_standard_deviation_corrected(nums, expected_value),
#         len(nums),
#         confidence_prob / 2 + 0.5,
#     ),
# )

### эмпирическая функция распределения и её график

plot_function(nums, lambda x: empirical_distribution_function(x, nums), "tex/output/task1/distribution_function.png")
### Помощь для теха
path_to_analytical_func_tex = "tex/output/task1/analytical_func.tex"
with open(path_to_analytical_func_tex, "w") as f:
    f.write(
        get_latex_form_empirical_distribution_func(
            nums, lambda x: empirical_distribution_function(x, nums)
        )
    )
print(
    f"Вид эмпирической функции распределения: записан в {path_to_analytical_func_tex}"
)


for i in range(1, 4 + 1):
    print(
        f"Центральный момент {i} порядка: "
        + str(round(moment_of_nth_order(nums, expected_value, i), ACCURACY))
    )

print(f"Мода: {get_mode(nums)}")
print(f"Медиана: {get_median(nums)}")

print(
    f"Коэффициент асимметрии: "
    + str(round(moment_of_nth_order(nums, expected_value, 3), ACCURACY))
)

print(
    f"Эксцесса: "
    + str(round(moment_of_nth_order(nums, expected_value, 4) - 3, ACCURACY))
)

#Выводы



# # --------------------------------------------------------
# hypothetical_deviation = compute_theoretical_values(nums, bin_count)
# print(f"Фактическое значение хи_H гипотезы по кр. Пирсона: {hypothetical_deviation}")

# critical_value = 14.4
# print(f"Хи критическое по кр. Пирсона (alpha = 0.025, 9-3) = {critical_value}")

# if (hypothetical_deviation < critical_value):
#     print(f"{hypothetical_deviation} < {critical_value} => гипотеза норм. распр. выполняется")
# else:
#     print(f"{hypothetical_deviation} >= {critical_value} => гипотеза норм. распр. НЕ выполняется")
