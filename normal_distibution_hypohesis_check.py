

# приняв в качестве нулевой гипотезы Н0: генеральная совокупность
# из которой извлечена выборка, имеет нормальное
# распределение, проверить ее, пользуясь критерием Пирсона
# при ровне значимости α 0,025

from interval_series import *
from sample_functions import *

def compute_theoretical_values(nums: list[float], count: int):
    whole_range = get_whole_range(nums)
    average = get_expected_value_estimate(nums)
    #m_i
    series = get_interval_statistical_series(whole_range, count, nums)
    #h
    interval_length = get_interval_length(whole_range, count);

    interval_boarders = get_interval_boarders(whole_range, count, nums)
    #sigma (с.к.о.)
    value_deviation = get_sample_standard_deviation(nums, average);

    # середины частотных интервалов
    x_i = get_interval_centers(interval_boarders)
    u_i = []
    for i in range(count):
        u_i.append((x_i[i] - average) / value_deviation)
    #m'_i
    theoretical_series = []
    for i in range(count):
        theoretical_series.append(
            (len(nums) * interval_length / value_deviation) *
            phi_function(u_i[i]))

    hypothetical_deviation = 0
    for i in range(count):
        hypothetical_deviation += ((series[i] - theoretical_series[i])**2)/theoretical_series[i]

    x_i_table = dict()
    for i in range(count):
        x_i_table[i+1] = dict()
        (x_i_table.get(i+1))["x_i"] = round(x_i[i], 2)
        (x_i_table.get(i+1))["u_i"] = round(u_i[i], 2)
        (x_i_table.get(i+1))["phi(u_i)"] = round(phi_function(u_i[i]), 2)
        (x_i_table.get(i+1))["m'_i"] = round(theoretical_series[i], 2)

    for i in range(count):
        print(f"{i+1}: {x_i_table[i+1]}")

    print("-------------------------------------")

    m_i_table = dict()
    for i in range(count):
        m_i_table[i+1] = dict()
        # res_table[i]
        (m_i_table.get(i+1))["m_i"] = round(series[i],2)
        (m_i_table.get(i+1))["m'_i"] = round(theoretical_series[i],2)
        (m_i_table.get(i+1))["m_i - m'_i"] = round(series[i] - theoretical_series[i],2)
        (m_i_table.get(i+1))["(m_i - m'_i)^2"] = round((series[i] - theoretical_series[i])**2,2)
        (m_i_table.get(i+1))["(m_i - m'_i)^2/m'_i"] = round(((series[i] - theoretical_series[i])**2)/theoretical_series[i],2)

    for i in range(count):
        print(f"{i+1}: {m_i_table[i+1]}")

    return hypothetical_deviation


def phi_function(x: float):
    return (1/math.sqrt(2*math.pi))*math.exp((-x**2)/2);
