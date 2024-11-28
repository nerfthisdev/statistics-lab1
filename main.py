import math
import matplotlib.pyplot as plt

### Вариант 3: (3,16)-(3,25)

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

print("Выборочный ряд:")
print(get_variation_series_pretty(nums))
print(get_extremes(nums))
print("Размах: {:.2f}".format(get_whole_range(nums)))
print(f"Мода: {get_mode(nums)}")
# print(f"Cтатистический ряд: {get_statistical_series(nums)}")

### оценки математического ожидания и среднеквадратического отклонения

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

def empirical_distribution_function(x: float, data: list[float]) -> float:
    count = 0
    
    for value in data:
        if value < x:
            count += 1
    
    return count / len(data)

def plot_function(nums: list[float], func):
    x_values = nums.copy()
    x_values.append(min(nums)-0.5)
    x_values.append(max(nums)+0.5)
    x_values.sort()

    y = [func(x) for x in x_values]

    plt.step(x_values, y)
    plt.ylabel("F^{*}(x)")
    plt.title("Эмпирическая функция распределения")
    plt.grid(True)
    plt.savefig("output/distribution_function.png")
    plt.close()

plot_function(nums, lambda x: empirical_distribution_function(x, nums))

### гистограмма и полигон приведенных частот группированной выборки

def get_interval_count(nums: list[float]) -> int:
    return math.ceil(1 + math.log2(len(nums)))

def get_interval_length(nums: list[float]) -> float:
    whole_range = get_whole_range(nums)
    interval_count = get_interval_count(nums)
    # Исправленная формула Стреджеса для того чтобы учесть,
    # что интервалы начинаются с минимального значения минус длинна/2 
    return whole_range / (interval_count - 1)

def get_interval_statistical_series(nums: list[float]) -> list[int]:
    whole_range = get_whole_range(nums)
    # формула Стерджеса
    interval_count = get_interval_count(nums)
    interval_length = get_interval_length(nums)
    
    intervals_starting_point = min(nums) - interval_length/2
    
    result = [0]*(interval_count)
    
    for num in nums:
        interval_offset_from_zero = num - intervals_starting_point
        interval_coverage = whole_range + interval_length
        
        # [min - interval_length/2 max + interval_length/2] -> 
        # [0,1] -> [0, interval_count]
        interval_number = math.floor(
            interval_offset_from_zero / interval_coverage * (interval_count)
        )
        
        # print(f"{num}: {interval_offset_from_zero / interval_coverage * interval_count}")
        result[interval_number] +=1
    return result

def get_interval_boarders(nums: list[float]) -> list[float]:
    interval_count = get_interval_count(nums)
    interval_length = get_interval_length(nums)
    intervals_starting_point = min(nums) - interval_length/2
    
    result = []
    
    for i in range(interval_count + 1):
        result.append(round(intervals_starting_point + interval_length*i, 4))
    
    return result

def get_statistical_interval_series(nums: list[float]) -> dict[str, float]:
    boarders = get_interval_boarders(nums)
    series = get_interval_statistical_series(nums)
    
    output = dict[str, float]()
    
    for i in range(len(series)):
        output[f"[{boarders[i]}, {boarders[i+1]})"] = series[i]
    
    return output

def plot_histogram(nums: list[float]) -> None:
    interval_count = get_interval_count(nums)
    interval_length = get_interval_length(nums)
    
    print(f"Количество интервалов: {interval_count}")
    print("Длина интервала: {:.2f}".format(interval_length))
    
    # intervals_starting_point = min(nums) - interval_length/2
    # Центры интервалов для полигона
    bin_centers = []
    for i in range(interval_count):
        # bin_centers.append(intervals_starting_point + 
        #                 interval_length*(i+1) - interval_length/2)
        
        # interval_length/2 сокращаются
        bin_centers.append(min(nums) + interval_length*(i+1))
    
    hist_density = [x/(len(nums)*interval_length) for x in 
                    get_interval_statistical_series(nums)]
    
    # Построение графика гистограммы
    plt.bar(bin_centers, hist_density, width=interval_length, 
            edgecolor='black', alpha=0.7, label="Гистограмма частот")

    # Построение полигона частот
    plt.plot(bin_centers, hist_density, marker='o', 
            color='blue', label="Полигон частот")

    # Подписи осей и график
    plt.xlabel("Значение")
    plt.ylabel("Плотность частоты")
    plt.title("Гистограмма частот и полигон частот")
    plt.legend()
    plt.grid(True)
    plt.savefig("output/histogram.png")
    
plot_histogram(nums)

### Помощь для теха

def get_latex_form_empirical_distribution_func(nums: list[float], func) -> str:
    sorted_nums = get_variation_series(set(nums))
    
    output = "F^*(x) = \\begin{cases}\n"
    output +=f"0, x < {sorted_nums[0]}\\\\\n"
    for i in range(len(sorted_nums) - 1):
        output += f"    {round(func(sorted_nums[i]), 3)},\\quad {sorted_nums[i]} \leq x < {sorted_nums[i+1]} \\\\\n"
    output += f"    1,\\quad x \geq {sorted_nums[-1]} \\\\\n"
    output += "\\end{cases}\n"
    return output

path_to_analytical_func_tex = "output/analytical_func.tex" 
with open(path_to_analytical_func_tex, "w") as f:
    f.write(get_latex_form_empirical_distribution_func(nums, 
        lambda x: empirical_distribution_function(x, nums)))
print(f"Вид эмпирической функции распределения: записан в {path_to_analytical_func_tex}")


def dict_to_latex_table(data: dict[any, any]) -> str:    
    table_size = 10
    dict_len = len(data.keys());
    
    output = "\\begin{tabular}{|" + "|".join(["c"]*dict_len) + "|}\n"
    count = 0
    key_row: list[str] = []
    value_row: list[str] = []
    
    for key, value in data.items():
        count += 1
            
        key_row.append(str(key))
        value_row.append(str(value))
        
        if (count % table_size == 0 or count == dict_len):
            output += f"    \\hline\n"
            output += f"    {' & '.join(key_row)}\\\\\n"
            output += f"    \\hline\n"
            output += f"    {' & '.join(value_row)}\\\\\n"
            output += f"    \\hline\n"
            
            key_row.clear()
            value_row.clear()
            
            if (count != dict_len - 1):
                output += f"    [1ex]\n"
    
    output += "\\end{tabular}"
    return output

path_to_statistical_interval_series_tex = "output/statistical_series.tex"
with open("output/statistical_interval_series.tex", "w") as f:
    output = dict_to_latex_table(get_statistical_interval_series(nums))
    f.write(output)
print(f"Интервальный ряд: записаны в {path_to_statistical_interval_series_tex}")

path_to_statistical_series = "output/statistical_series.tex"
with open(path_to_statistical_series, "w") as f:
    output = dict_to_latex_table(get_statistical_series(nums))
    f.write(output)
print(f"Статистический ряд: записаны в {path_to_statistical_series}")


