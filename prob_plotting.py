from typing import List
import matplotlib.pyplot as plt

from interval_series import *


def plot_histogram_with_mode(
    whole_range: float,
    count: int,
    nums: list[float],
    file_name: str,
    mode: float | None = None,
) -> None:
    interval_length = get_interval_length(whole_range, count)
    interval_boarders = get_interval_boarders(whole_range, count, nums)

    bin_centers = get_interval_centers(interval_boarders)

    hist_density = [
        x / (len(nums) * interval_length)
        for x in get_interval_statistical_series(whole_range, count, nums)
    ]

    plt.bar(
        bin_centers,
        hist_density,
        width=interval_length,
        edgecolor="black",
        alpha=0.7,
        label="Гистограмма частот",
    )

    plt.plot(
        bin_centers, hist_density, marker="o", color="blue", label="Полигон частот"
    )

    if mode is not None:
        plt.axvline(
            mode, color="red", linestyle="--", linewidth=2, label=f"Мода ({mode:.2f})"
        )

    # Подписи осей и график
    plt.xlabel("Значение")
    plt.ylabel("Плотность частоты")
    plt.title("Гистограмма частот и полигон частот")
    plt.legend()
    plt.grid(True)
    save_fig_to_pdf_and_png(file_name)
    plt.close()


def plot_polygon(x_vals: list[float], y_vals: list[float], file_name: str):
    if len(x_vals) != len(y_vals):
        print("ERROR: x_vals: list[float] != y_vals: list[float]")
        return

    # Построение полигона частот
    plt.plot(x_vals, y_vals, marker="o", color="blue", label="Полигон")

    plt.legend()
    plt.grid(True)
    save_fig_to_pdf_and_png(file_name)
    plt.close()


def plot_function(nums: list[float], func, file_path: str):
    x_values = nums.copy()
    x_values.append(min(nums) - 0.5)
    x_values.append(max(nums) + 0.5)
    x_values.sort()

    y = [func(x) for x in x_values]

    plt.step(x_values, y)
    plt.ylabel("F^{*}(x)")
    plt.title("Эмпирическая функция распределения")
    plt.grid(True)
    save_fig_to_pdf_and_png(file_path)
    plt.close()


def plot_cumulative_with_median(
    whole_range: float,
    count: int,
    nums: list[float],
    file_name: str,
    median_value: float | None = None,
) -> None:
    interval_boarders = get_interval_boarders(whole_range, count, nums)

    # Центры интервалов для полигона
    bin_centers = get_interval_centers(interval_boarders)
    interval_density = get_interval_statistical_series(whole_range, count, nums)
    prev = 0
    cumulative_values = list[float]()
    for i in range(len(interval_density)):
        prev += interval_density[i]
        cumulative_values.append(prev)

    plt.plot(
        bin_centers,
        cumulative_values,
        marker="o",
        color="blue",
        label="Кумулятивная кривая",
    )

    if median_value is not None:
        plt.axvline(
            x=median_value,
            color="red",
            linestyle="--",
            linewidth=1.5,
            label=f"Медиана ({median_value:.2f})",
        )

    plt.xlabel("Значение")
    plt.ylabel("Накопленная частота")
    plt.title("Кумулята с медианой")
    plt.legend()
    plt.grid(True)
    save_fig_to_pdf_and_png(file_name)
    plt.close()


def plot_ogive(
    whole_range: float,
    count: int,
    nums: list[float],
    file_name: str,
    median_value: float | None = None,
) -> None:
    interval_boarders = get_interval_boarders(whole_range, count, nums)

    bin_centers = get_interval_centers(interval_boarders)
    interval_density = get_interval_statistical_series(whole_range, count, nums)
    prev = 0
    cumulative_values = list[float]()
    for i in range(len(interval_density)):
        prev += interval_density[i]
        cumulative_values.append(prev)

    plt.plot(
        cumulative_values, bin_centers, marker="o", color="blue", label="Полигон частот"
    )

    if median_value is not None:
        plt.axhline(
            y=median_value,
            color="red",
            linestyle="--",
            linewidth=1.5,
            label=f"Медиана ({median_value:.2f})",
        )

    plt.xlabel("Накопленная частота")
    plt.ylabel("Значение")
    plt.title("Огива")
    plt.legend()
    plt.grid(True)
    save_fig_to_pdf_and_png(file_name)
    plt.close()


def boxplot_for_two_lists(list1: List[float], list2: List[float], file_path: str):
    # Создаем график с двумя subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Боксплот для первого набора данных
    ax1.boxplot(list1, vert=True, patch_artist=True)
    ax1.set_title("Первый набор данных")
    ax1.set_ylabel("Значения")
    ax1.grid(True)

    ax2.boxplot(list2, vert=True, patch_artist=True)
    ax2.set_title("Второй набор данных")
    ax2.grid(True)

    plt.suptitle("Сравнение распределений данных")
    plt.tight_layout()

    save_fig_to_pdf_and_png(file_path)
    plt.close()


def save_fig_to_pdf_and_png(file_path: str) -> None:
    plt.savefig(file_path)
    if file_path.endswith(".png"):
        file_path = file_path[: -len(".png")] + ".pdf"
    else:
        file_path = file_path[: -len(".pdf")] + ".png"
    plt.savefig(file_path)
