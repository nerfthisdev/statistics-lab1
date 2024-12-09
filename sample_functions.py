import math


def get_variation_series(nums: list[float]):
    return sorted(nums)

def get_variation_series_pretty(nums: list[float]):
    return " ≤ ".join(map(str, get_variation_series(nums)))

def get_whole_range(nums: list[float]):
    return max(nums) - min(nums)

def get_extremes(nums: list[float]):
    sorted_nums: list[float] = get_variation_series(nums)

    output_str: str =  f"min: {sorted_nums[0]} "
    output_str += f"max: {sorted_nums[-1]} "

    return output_str

def get_statistical_series(nums) -> dict[float, int]:
    number_freq = dict()
    for num in nums:
        if (number_freq.get(num, None) == None):
            number_freq[num] = 0
        number_freq[num] += 1
    return number_freq

def get_mode(nums: list[float]) -> float | None:
    number_freq = get_statistical_series(nums)

    max_occurrences = max(value for key, value in number_freq.items())

    for key, value in number_freq.items():
        if value == max_occurrences:
            return key
    return None


def get_expected_value_estimate(nums: list[float]) -> float:
    #просто средне арифметическое
    return (1 / len(nums)) * sum(nums)

def get_expected_value_deviation(nums: list[float]) -> float:
    #просто средне арифметическое
    expected_value = get_expected_value_estimate(nums)

    return sum(x - expected_value for x in nums)

# Выборочная дисперсия
def get_sample_variance(nums: list[float], expected_value: float) -> float:
    # тут не нужно умножать на n_i (частоту значения), потому что
    # мы пользуемся массивом (с повторяющимися элементами), а не множеством
    return sum(map(lambda x: (x - expected_value) ** 2, nums)) / len(nums)

# Выборочное среднеквадратическое отклонение
def get_sample_standard_deviation(nums: list[float], expected_value: float):
    sample_variance = get_sample_variance(nums, expected_value)
    return math.sqrt(sample_variance)


# Выборочное среднеквадратическое отклонение (исправленная)
def get_sample_standard_deviation_corrected(nums: list[float], expected_value: float) -> float:
    sample_variance = get_sample_variance(nums, expected_value)
    return math.sqrt(sample_variance * (len(nums) / (len(nums) - 1)))

def empirical_distribution_function(x: float, data: list[float]) -> float:
    count = 0

    for value in data:
        if value < x:
            count += 1

    return count / len(data)
