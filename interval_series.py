
import math

from sample_functions import get_whole_range

def get_interval_count_by_sturgess(n: int) -> int:
    return math.ceil(1 + math.log2(n))

def get_whole_range_with_offsets(nums):
    whole_range = get_whole_range(nums)
    count = get_interval_count_by_sturgess(len(nums))
    print(f"Количество интервалов по ф. Стерджесса: {count}")
    # print("Длина интервала для покрытия с отступом: {:.2f}".format(interval_length))
    return whole_range + get_interval_length(whole_range, count)

def get_interval_length(whole_range: float, count: int) -> float:
    return whole_range / count

def get_intervals_starting_point(whole_range: float, nums: list[float]) -> float:
    return min(nums) - (whole_range - (max(nums) - min(nums)))/2

def get_interval_statistical_series_new(whole_range: float, count: int, nums: list[float]) -> list[float]:
    # interval_length = get_interval_length(whole_range, count)
    intervals_starting_point = get_intervals_starting_point(whole_range, nums)

    result = [0]*(count)

    for num in nums:
        interval_offset_from_zero = num - intervals_starting_point
        # [min - interval_length/2 max + interval_length/2] ->
        # [0,1] -> [0, interval_count]
        interval_number = math.floor(
            interval_offset_from_zero / whole_range * (count)
        )

        if (interval_number == count):
            #самую правую границу включим
            interval_number = count - 1

        result[interval_number] +=1
    return result


def get_interval_boarders_new(whole_range: float, count: int,  nums: list[float]) -> list[float]:
    intervals_starting_point = get_intervals_starting_point(whole_range, nums)
    interval_length = get_interval_length(whole_range, count)
    result = []
    for i in range(count+1):
        result.append(intervals_starting_point + interval_length*i)
    return result


# def get_interval_boarders(nums: list[float]) -> list[float]:
#     interval_count = get_interval_count_by_sturgess(nums)
#     interval_length = get_sturgess_interval_length_with_offset(nums)
#     intervals_starting_point = min(nums) - interval_length/2

#     result = []

#     for i in range(interval_count + 1):
#         result.append(round(intervals_starting_point + interval_length*i, 4))

#     return result


def get_statistical_interval_series_new(whole_range: float, count: int, nums: list[float]) -> dict[str, float]:
    boarders = get_interval_boarders_new(whole_range, count, nums)
    series = get_interval_statistical_series_new(whole_range, count, nums)

    output = dict[str, float]()

    for i in range(len(series)):
        output[f"[{boarders[i]}, {boarders[i+1]})"] = series[i]

    return output
