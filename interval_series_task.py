from latex_generator import dict_to_latex_table_str
from nums import get_second_nums
from prob_plotting import (
    plot_cumulative_with_median,
    plot_function,
    plot_histogram_with_mode,
    plot_ogive,
)
from variation_series import (
    empirical_distribution_function,
    get_extremes,
    get_whole_range,
)
from interval_series import *

# 2. Для выборки В:
# - указать максимальный и минимальный элементы выборки, найти размах выборки;
# - определить оптимальное количество интервалов группировки и длину интервала группировки;
# - построить интервальный ряд и гистограмму, а также полигон ряда;
# - записать эмпирическую функцию распределения и построить её график, построить кумуляту (и огиву);
# - вычислить начальные и центральные эмпирические моменты до 4-го порядка;
# - найти моду (отметить на гистограмме), медиану (отметить на кумуляте), коэффициенты асимметрии и эксцесса;
# - сделать выводы и сформулировать гипотезы о распределении генеральной совокупности из которой извлечена выборка, оценить параметры этого распределения.

# - если ряд интервальный, то функция распределения должна совпадать с кумулятой и не быть ступенчатой
# - x^{*} - середина интервала


def make_task2(precision):
    nums = get_second_nums()

    plot_function(
        nums,
        lambda x: empirical_distribution_function(x, nums),
        "tex/output/task2/distribution_function.pdf",
    )

    whole_range = get_whole_range(nums)
    print(f"n = {len(nums)}")

    print(get_extremes(nums))
    print("Размах: {:.2f}".format(whole_range))

    bin_count: int = get_interval_count_by_sturgess(len(nums))
    interval_length: float = whole_range / bin_count

    print("Оптимальное количество интервалов (по ф. Стерджесса): " + str(bin_count))
    print("Длинна интервала: " + str(interval_length))

    path_to_statistical_interval_series_test_tex = (
        f"tex/output/task2/statistical_interval_series_{bin_count}_bins.tex"
    )
    with open(path_to_statistical_interval_series_test_tex, "w") as f:
        output = dict_to_latex_table_str(
            get_statistical_interval_series(whole_range, bin_count, nums)
        )
        f.write(output)
    print(
        f"Интервальный статистический ряд: записаны в {path_to_statistical_interval_series_test_tex}"
    )

    interval_boarders: list[float] = get_interval_boarders(whole_range, bin_count, nums)
    bin_centers = get_interval_centers(interval_boarders)
    statistical_series = get_interval_statistical_series(whole_range, bin_count, nums)

    expected_value = get_expected_value_from_interval_series(
        len(nums), bin_centers, statistical_series
    )

    print("Начальный момент (среднее): " + str(round(expected_value, precision)))

    sample_variance = get_sample_variance_from_interval_series(
        n=len(nums),
        expected_value=expected_value,
        bin_centers=bin_centers,
        interval_statistical_series=statistical_series,
    )

    standard_deviation = get_sample_standard_deviation(sample_variance)

    for i in range(1, 4 + 1):
        print(
            f"Центральный эмпирический момент {i}-того порядка: "
            + str(
                round(
                    get_nth_moment_from_interval_series(
                        moment=i,
                        n=len(nums),
                        expected_value=expected_value,
                        standard_deviation=standard_deviation,
                        bin_centers=bin_centers,
                        interval_statistical_series=statistical_series,
                    ),
                    precision,
                )
            )
        )

    asymmetry_coefficient = get_nth_moment_from_interval_series(
        moment=3,
        n=len(nums),
        expected_value=expected_value,
        standard_deviation=standard_deviation,
        bin_centers=bin_centers,
        interval_statistical_series=statistical_series,
    )

    print(f"Коэффициент асимметрии: {round(asymmetry_coefficient,precision)}")

    kurtosis = (
        get_nth_moment_from_interval_series(
            moment=4,
            n=len(nums),
            expected_value=expected_value,
            standard_deviation=standard_deviation,
            bin_centers=bin_centers,
            interval_statistical_series=statistical_series,
        )
        - 3
    )

    print(f"Эксцесс: {round(kurtosis, precision)}")

    mode = get_mode_from_interval_series(
        interval_length=interval_length,
        interval_statistical_series=statistical_series,
        interval_borders=interval_boarders,
    )
    print(f"Мода: {round(mode,precision)}")

    median = get_median_from_interval_series(
        n=len(nums),
        interval_length=interval_length,
        interval_statistical_series=statistical_series,
        interval_borders=interval_boarders,
    )
    print(f"Медиана: {round(median,precision)}")

    path_to_histogram = f"tex/output/task2/histogram_{bin_count}_bins.pdf"
    plot_histogram_with_mode(whole_range, bin_count, nums, path_to_histogram, mode)
    print(f"Гистограмма записана в {path_to_histogram}")

    path_to_cumulative = f"tex/output/task2/cumulative_{bin_count}_bins.pdf"
    plot_cumulative_with_median(
        whole_range, bin_count, nums, path_to_cumulative, median
    )
    print(f"Кумулята записана в {path_to_cumulative}")

    path_to_ogive = f"tex/output/task2/ogive_{bin_count}_bins.pdf"
    plot_ogive(whole_range, bin_count, nums, path_to_ogive, median)
    print(f"Огива записана в {path_to_ogive}")
