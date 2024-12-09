import matplotlib.pyplot as plt

from interval_series import *

# from main import get_interval_count, get_interval_length, get_interval_statistical_series

# def plot_histogram_with_sturgess(nums: list[float]) -> None:


def plot_histogram(whole_range: float, count: int, nums: list[float]) -> None:
    # interval_count = get_interval_count_by_sturgess(nums)
    interval_length = get_interval_length(whole_range, count)

    # print(f"Количество интервалов по ф. Стерджесса: {interval_count}")
    # print("Длина интервала для покрытия с отступом: {:.2f}".format(interval_length))

    # intervals_starting_point = min(nums) - interval_length/2
    # Центры интервалов для полигона
    bin_centers = []
    for i in range(count):
        # bin_centers.append(intervals_starting_point +
        #                 interval_length*(i+1) - interval_length/2)

        # interval_length/2 сокращаются
        bin_centers.append(min(nums) + interval_length*(i+1))

    hist_density = [x/(len(nums)*interval_length) for x in
                    get_interval_statistical_series_new(whole_range, count, nums)]

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
