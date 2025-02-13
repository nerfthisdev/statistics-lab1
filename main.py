from interval_series import *
from latex_generator import *
from normal_distibution_hypohesis_check import compute_theoretical_values
from nums import get_matstat_nums
from prob_plotting import *
from sample_functions import *

nums = get_matstat_nums()

print(len(nums))

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
print(f"Медиана: {get_median(nums)}")

### оценки математического ожидания и среднеквадратического отклонения
expected_value = get_expected_value_estimate(nums)
confidence_prob = 0.9

print("Оценка математического ожидания: {:.2f}"
    .format(expected_value))

path_to_expected_value_trusted_interval = "tex/output/expected_value_trusted_interval.tex"
with open(path_to_expected_value_trusted_interval, "w") as f:
    output = get_confidence_interval_for_expvalue_large_set_with_latex_steps(
        expected_value,
        len(nums),
        get_sample_standard_deviation_corrected(nums, expected_value),
        confidence_prob)

    f.write(output)
print(f"Доверительный интервал мат. ожидания с доверительной вероятностью ɣ={confidence_prob}: записаны в {path_to_expected_value_trusted_interval}")


print("Стандартное отклонение {:.2f}"
    .format(get_expected_value_deviation(nums)))
print("Дисперсия {:.4f}"
    .format(get_sample_variance(nums, expected_value)))
print("Оценка выборочного среднеквадратического отклонения: {:.4f}"
    .format(get_sample_standard_deviation(nums, expected_value)))
print("Оценка выборочного с.к.о. (исправленная): {:.4f}"
    .format(get_sample_standard_deviation_corrected(nums, expected_value)))
print(f"Доверительный интервал с.к.о.с доверительной вероятностью ɣ=\n{confidence_prob}",
    get_confidence_interval_for_standard_deviation(
        get_sample_standard_deviation_corrected(nums, expected_value),
        len(nums),
        confidence_prob/2 + 0.5
        )
    )

### эмпирическая функция распределения и её график
plot_function(nums, lambda x: empirical_distribution_function(x, nums))

### гистограмма и полигон приведенных частот группированной выборки

plot_histogram_with_sturgess(nums, "tex/output/histogram_sturgess.png")

bin_count = 8

plot_histogram(
    get_whole_range(nums),
    bin_count,
    nums,
    f"tex/output/histogram_{bin_count}_bins.png"
)

plot_cumulative(
    get_whole_range(nums),
    bin_count,
    nums,
    f"tex/output/cumulative_{bin_count}_bins.png"
)



### Помощь для теха
path_to_analytical_func_tex = "tex/output/analytical_func.tex"
with open(path_to_analytical_func_tex, "w") as f:
    f.write(get_latex_form_empirical_distribution_func(nums,
        lambda x: empirical_distribution_function(x, nums)))
print(f"Вид эмпирической функции распределения: записан в {path_to_analytical_func_tex}")

path_to_statistical_interval_series_tex = "tex/output/statistical_interval_series.tex"
with open(path_to_statistical_interval_series_tex, "w") as f:
    output = dict_to_latex_table_str(
        get_statistical_interval_series(
            get_whole_range_with_offsets(nums),
            get_interval_count_by_sturgess(len(nums)),
            nums))

    f.write(output)
print(f"Интервальный ряд: записаны в {path_to_statistical_interval_series_tex}")

path_to_statistical_series = "tex/output/statistical_series_sturgess.tex"
with open(path_to_statistical_series, "w") as f:
    output = dict_to_latex_table_str(get_statistical_series(nums))
    f.write(output)
print(f"Статистический ряд: записаны в {path_to_statistical_series}")

path_to_statistical_interval_series_test_tex = f"tex/output/statistical_interval_series_{bin_count}_bins.tex"
with open(path_to_statistical_interval_series_test_tex, "w") as f:
    output = dict_to_latex_table_str(get_statistical_interval_series(get_whole_range(nums), bin_count, nums))
    f.write(output)
print(f"Интервальный ряд: записаны в {path_to_statistical_interval_series_test_tex}")


# --------------------------------------------------------
hypothetical_deviation = compute_theoretical_values(nums, bin_count)
print(f"Фактическое значение хи_H гипотезы по кр. Пирсона: {hypothetical_deviation}")

critical_value = 14.4
print(f"Хи критическое по кр. Пирсона (alpha = 0.025, 9-3) = {critical_value}")

if (hypothetical_deviation < critical_value):
    print(f"{hypothetical_deviation} < {critical_value} => гипотеза норм. распр. выполняется")
else:
    print(f"{hypothetical_deviation} >= {critical_value} => гипотеза норм. распр. НЕ выполняется")
