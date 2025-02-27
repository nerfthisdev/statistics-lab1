from collections import OrderedDict
import math

import scipy
import numpy as np
from q_table import get_q_table_value

np.set_printoptions(legacy="1.25")


def get_variation_series(nums: list[float]):
    return sorted(nums)


def get_variation_series_pretty(nums: list[float]):
    return " ≤ ".join(map(str, get_variation_series(nums)))


def get_whole_range(nums: list[float]):
    return max(nums) - min(nums)


def get_extremes(nums: list[float]):
    sorted_nums: list[float] = get_variation_series(nums)

    output_str: str = f"min: {sorted_nums[0]} "
    output_str += f"max: {sorted_nums[-1]} "

    return output_str


def get_statistical_series(nums) -> dict[float, int]:
    number_freq = dict()
    for num in nums:
        if number_freq.get(num, None) == None:
            number_freq[num] = 0
        number_freq[num] += 1
    return OrderedDict(sorted(number_freq.items()))


def get_mode(nums: list[float]) -> float | None:
    number_freq = get_statistical_series(nums)

    max_occurrences = max(value for key, value in number_freq.items())

    for key, value in number_freq.items():
        if value == max_occurrences:
            return key
    return None


def get_median(nums: list[float]):
    sorted_nums: list[float] = get_variation_series(nums)

    if len(sorted_nums) % 2 == 0:
        median_index: int = math.floor(len(sorted_nums) / 2)

        return (nums[median_index] + nums[median_index + 1]) / 2
    else:
        median_index: int = math.floor(len(sorted_nums) / 2)

        return nums[median_index]


def get_expected_value_estimate(nums: list[float]) -> float:
    # просто средне арифметическое
    return (1 / len(nums)) * sum(nums)


def get_expected_value_deviation(nums: list[float]) -> float:
    # просто средне арифметическое
    expected_value = get_expected_value_estimate(nums)

    return sum(x - expected_value for x in nums)


# Выборочная дисперсия
def get_sample_variance(nums: list[float], expected_value: float) -> float:
    # тут не нужно умножать на n_i (частоту значения), потому что
    # мы пользуемся массивом (с повторяющимися элементами), а не множеством
    return sum(map(lambda x: (x - expected_value) ** 2, nums)) / len(nums)


def moment_of_nth_order(nums: list[float], expected_value: float, nth_order: int):
    return sum(map(lambda x: (x - expected_value) ** nth_order, nums)) / len(nums)


# Выборочное среднеквадратическое отклонение
def get_sample_standard_deviation(nums: list[float], expected_value: float):
    sample_variance = get_sample_variance(nums, expected_value)
    return math.sqrt(sample_variance)


# Выборочное среднеквадратическое отклонение (исправленная)
def get_sample_standard_deviation_corrected(
    nums: list[float], expected_value: float
) -> float:
    sample_variance = get_sample_variance(nums, expected_value)
    return math.sqrt(sample_variance * (len(nums) / (len(nums) - 1)))


def empirical_distribution_function(x: float, data: list[float]) -> float:
    count = 0

    for value in data:
        if value < x:
            count += 1

    return count / len(data)


def laplace_function(x: float) -> float:
    return scipy.stats.norm.cdf(x)


def student_coefficient(gamma, n):
    return scipy.stats.t.ppf(gamma, n)


def laplace_normalized_function(x: float) -> float:
    return laplace_function(x) - 0.5


def get_inverse_laplace(alpha: float):
    error_margin = 0.0001
    # начальное значение - половина от максимального
    step = 4 / 2

    last_point = step
    last_value = 0
    while math.fabs(last_value - alpha) > error_margin:
        last_value = laplace_function(last_point)

        if last_value < alpha:
            last_point += step
        if last_value >= alpha:
            last_point -= step

        step = step / 2

    return last_point


def get_confidence_interval_for_expvalue(
    average_value: float, n: int, sigma: float, confidence_prob: float
) -> tuple[float, float]:
    t_gamma = 0
    if n <= 30:
        t_gamma = student_coefficient(confidence_prob / 2 + 0.5, n - 1)
    else:
        t_gamma = get_inverse_laplace(confidence_prob / 2 + 0.5)

    res = t_gamma * sigma / math.sqrt(n)
    return average_value - res, average_value + res


def get_confidence_interval_for_standard_deviation(
    sigma_corrected: float, n: int, gamma: float
) -> tuple[float, float]:
    q = get_q_table_value(gamma, n)
    if q < 1:
        return sigma_corrected * (1 - q), sigma_corrected * (1 + q)
    else:
        return 0, sigma_corrected * (1 + q)
