import matplotlib.pyplot as plt

from interval_series import get_interval_count, get_interval_length, get_interval_statistical_series

# from main import get_interval_count, get_interval_length, get_interval_statistical_series


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
