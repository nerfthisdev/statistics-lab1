import math

from variation_series import get_whole_range


def get_interval_count_by_sturgess(n: int) -> int:
    return math.floor(1 + math.log2(n))


def get_whole_range_with_offsets(nums):
    whole_range = get_whole_range(nums)
    count = get_interval_count_by_sturgess(len(nums))
    print(f"Количество интервалов по ф. Стерджесса: {count}")
    # print("Длина интервала для покрытия с отступом: {:.2f}".format(interval_length))
    return whole_range + get_interval_length(whole_range, count)


def get_interval_length(whole_range: float, count: int) -> float:
    return whole_range / count


def get_intervals_starting_point(whole_range: float, nums: list[float]) -> float:
    return min(nums) - (whole_range - (max(nums) - min(nums))) / 2


def get_interval_statistical_series(
    whole_range: float, count: int, nums: list[float]
) -> list[float]:
    # interval_length = get_interval_length(whole_range, count)
    intervals_starting_point = get_intervals_starting_point(whole_range, nums)

    result = [0] * (count)

    for num in nums:
        interval_offset_from_zero = num - intervals_starting_point
        # [min - interval_length/2 max + interval_length/2] ->
        # [0,1] -> [0, interval_count]
        interval_number = math.floor(interval_offset_from_zero / whole_range * (count))

        if interval_number == count:
            # самую правую границу включим
            interval_number = count - 1

        result[interval_number] += 1
    return result


def get_interval_boarders(
    whole_range: float, count: int, nums: list[float]
) -> list[float]:
    intervals_starting_point = get_intervals_starting_point(whole_range, nums)
    interval_length = get_interval_length(whole_range, count)
    result = []
    for i in range(count + 1):
        result.append(intervals_starting_point + interval_length * i)
    return result


def get_statistical_interval_series(
    whole_range: float, count: int, nums: list[float]
) -> dict[str, float]:
    boarders = get_interval_boarders(whole_range, count, nums)
    series = get_interval_statistical_series(whole_range, count, nums)

    output = dict[str, float]()

    for i in range(len(series)):
        output[f"[{boarders[i]}, {boarders[i+1]})"] = series[i]

    return output


def get_interval_centers(interval_boarders: list[float]):
    bin_centers = []
    for i in range(len(interval_boarders) - 1):
        bin_centers.append((interval_boarders[i] + interval_boarders[i + 1]) / 2)

    return bin_centers


def get_expected_value_from_interval_series(
    n: int, bin_centers: list[float], interval_statistical_series: list[float]
):
    if len(bin_centers) != len(interval_statistical_series):
        print("ERROR! len(bin_centers) != len(interval_statistical_series)")
        return

    interval_count = len(bin_centers)
    res = 0
    for i in range(interval_count):
        res += bin_centers[i] * interval_statistical_series[i]

    return res / n


def get_mode_from_interval_series(
    interval_length: float,
    interval_borders: list[float],
    interval_statistical_series: list[float],
):
    max_frequency = max(interval_statistical_series)
    modal_interval_index = interval_statistical_series.index(max_frequency)

    start_of_modal_interval = interval_borders[modal_interval_index]

    modal_interval_frequency = interval_statistical_series[modal_interval_index]
    modal_interval_minus_one_frequency = interval_statistical_series[
        modal_interval_index - 1
    ]
    modal_interval_plus_one_frequency = interval_statistical_series[
        modal_interval_index + 1
    ]

    return start_of_modal_interval + interval_length * (
        (modal_interval_frequency - modal_interval_minus_one_frequency)
        / (
            (modal_interval_frequency - modal_interval_minus_one_frequency)
            + (modal_interval_frequency - modal_interval_plus_one_frequency)
        )
    )


def get_median_from_interval_series(
    n: int,
    interval_length: float,
    interval_statistical_series: list[float],
    interval_borders: list[float],
):

    accum_interval_statistical_series = list[float]()

    prev_sum: float = 0
    for freq in interval_statistical_series:
        prev_sum += freq
        accum_interval_statistical_series.append(prev_sum)

    median_interval_index = 0
    for i in range(n):
        if accum_interval_statistical_series[i] > n / 2:
            median_interval_index = i
            break

    return interval_borders[median_interval_index] + interval_length * (
        (0.5 * n - accum_interval_statistical_series[median_interval_index - 1])
        / interval_statistical_series[median_interval_index]
    )


def get_sample_variance_from_interval_series(
    n: int,
    expected_value: float,
    bin_centers: list[float],
    interval_statistical_series: list[float],
):
    if len(bin_centers) != len(interval_statistical_series):
        print("ERROR! len(bin_centers) != len(interval_statistical_series)")
        return

    interval_count = len(bin_centers)
    res = 0
    for i in range(interval_count):
        res += (bin_centers[i] - expected_value) ** 2 * interval_statistical_series[i]

    return res / n


def get_sample_standard_deviation(sample_variance: float):
    return math.sqrt(sample_variance)


def get_nth_moment_from_interval_series(
    moment: int,
    n: int,
    expected_value: float,
    standard_deviation: float,
    bin_centers: list[float],
    interval_statistical_series: list[float],
):

    if len(bin_centers) != len(interval_statistical_series):
        print("ERROR! len(bin_centers) != len(interval_statistical_series)")
        return

    interval_count = len(bin_centers)
    res = 0
    for i in range(interval_count):
        res += (
            (bin_centers[i] - expected_value) ** moment
        ) * interval_statistical_series[i]

    return res / (n * (standard_deviation**moment))
