
import math

def get_whole_range(nums: list[float]):
    return max(nums) - min(nums)

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
