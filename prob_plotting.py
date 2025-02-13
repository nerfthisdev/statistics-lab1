import matplotlib.pyplot as plt

from interval_series import *

def plot_histogram_with_sturgess(nums: list[float], file_name: str) -> None:
    whole_range_with_offsets = get_whole_range_with_offsets(nums)

    plot_histogram(
        whole_range_with_offsets,
        get_interval_count_by_sturgess(len(nums)),
        nums,
        file_name)

def plot_histogram(whole_range: float, count: int, nums: list[float], file_name: str) -> None:
    interval_length = get_interval_length(whole_range, count)
    interval_boarders = get_interval_boarders(whole_range, count, nums)

    # Центры интервалов для полигона
    bin_centers = get_interval_centers(interval_boarders)

    hist_density = [x/(len(nums)*interval_length) for x in
                    get_interval_statistical_series(whole_range, count, nums)]

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
    plt.savefig(file_name)
    plt.close()

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
    plt.savefig("tex/output/distribution_function.png")
    plt.close()


def plot_cumulative(whole_range: float, count: int, nums: list[float], file_name: str) -> None:
    interval_length = get_interval_length(whole_range, count)
    interval_boarders = get_interval_boarders(whole_range, count, nums)

    # Центры интервалов для полигона
    bin_centers = get_interval_centers(interval_boarders)

    interval_density = get_interval_statistical_series(whole_range, count, nums)

    prev = 0
    cumulative_values = list[float]()
    for i in range(len(interval_density)):
        prev += interval_density[i]
        cumulative_values.append(prev)

    # Построение полигона частот
    plt.plot(bin_centers, cumulative_values, marker='o',
            color='blue', label="Полигон частот")

    # Подписи осей и график
    plt.xlabel("Значение")
    plt.ylabel("Плотность частоты")
    plt.title("Гистограмма частот и полигон частот")
    plt.legend()
    plt.grid(True)
    plt.savefig(file_name)
    plt.close()
