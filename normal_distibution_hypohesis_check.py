

# приняв в качестве нулевой гипотезы Н0: генеральная совокупность
# из которой извлечена выборка, имеет нормальное
# распределение, проверить ее, пользуясь критерием Пирсона
# при ровне значимости α 0,025

from interval_series import *
from latex_generator import *
from sample_functions import *

def compute_theoretical_values(nums: list[float], count: int):
    whole_range = get_whole_range(nums)
    average = round(get_expected_value_estimate(nums),2)
    #m_i
    n_i = get_interval_statistical_series(whole_range, count, nums)
    # interval_length = get_interval_length(whole_range, count);

    interval_boarders = get_interval_boarders(whole_range, count, nums)
    #sigma (с.к.о.)
    value_deviation = get_sample_standard_deviation_corrected(nums, average);


    z_i = dict()
    for i in range(2, count):
        z_i[i] = round((interval_boarders[i] - average)/value_deviation,2)

    z_i[1] = -math.inf
    z_i[count] = math.inf

    first_table = dict()
    for i in range(1, count):
        first_table[i] = dict()
        (first_table.get(i))[f"(x_{i}, x_{i+1})"] = (interval_boarders[i], interval_boarders[i+1])
        (first_table.get(i))[f"(x_{i} - x_{"{avg}"}, x_{i+1} - x_{"{avg}"})"] = (round(interval_boarders[i] - average,2), round((interval_boarders[i+1] - average),2))
        (first_table.get(i))[f"(z_{i}, z_{i+1})"] = (z_i[i], z_i[i+1])
        print(f"{i}: {first_table[i]}")
    compute_table_to_latex_table_str_to_file(first_table, "tex/output/hypophyses/first_table.tex")
    # print(f"{compute_table_to_latex_table_str(first_table)}")


    print("-----------------------------------------")
    n_i_shtrih = dict()
    P_i = dict()
    second_table = dict()
    for i in range(1, count):
        second_table[i] = dict()
        (second_table.get(i))[f"(z_{i}, z_{i+1})"] = (z_i[i], z_i[i+1])
        (second_table.get(i))[f"(\\Phi(z_{i})"] = round(laplace_normalized_function(z_i[i]),2)
        (second_table.get(i))[f"(\\Phi(z_{i+1})"] = round(laplace_normalized_function(z_i[i+1]),2)
        P_i[i] = laplace_normalized_function(z_i[i+1]) - laplace_normalized_function(z_i[i])
        (second_table.get(i))[f"P_{i}"] = round(P_i[i],2)
        n_i_shtrih[i] = len(nums)*(laplace_normalized_function(z_i[i+1]) - laplace_normalized_function(z_i[i]))
        (second_table.get(i))[f"n'_{i}"] = round(n_i_shtrih[i],2)
        print(f"{i}: {second_table[i]}")
    print(f"sum n_i' = {sum(n_i_shtrih.values())}")
    print(f"sum P_i = {sum(P_i.values())}")
    print("-------------------------------------")
    compute_table_to_latex_table_str_to_file(second_table, "tex/output/hypophyses/second_table.tex")

    m_i_table = dict()
    result_sum = 0
    for i in range(1, count):
        m_i_table[i] = dict()
        # res_table[i]
        (m_i_table.get(i))["n_i"] = round(n_i[i-1],2)
        (m_i_table.get(i))["n'_i"] = round(n_i_shtrih[i],2)
        (m_i_table.get(i))["n_i - n'_i"] = round(n_i[i-1] - n_i_shtrih[i],2)
        (m_i_table.get(i))["(n_i - n'_i)^2"] = round((n_i[i-1] - n_i_shtrih[i])**2,2)
        (m_i_table.get(i))["(n_i - n'_i)^2/n'_i"] = round(((n_i[i-1] - n_i_shtrih[i])**2)/n_i_shtrih[i],2)
        print(f"{i}: {m_i_table[i]}")
        result_sum += ((n_i[i-1] - n_i_shtrih[i])**2)/n_i_shtrih[i]

    compute_table_to_latex_table_str_to_file(m_i_table, "tex/output/hypophyses/m_i_table.tex")

    print(f"sum n_i = {sum(n_i)}")
    print(f"sum n'_i = {sum(n_i_shtrih.values())}")

    # for i in range(count):
    #     print(f"{i+1}: {m_i_table[i+1]}")

    return result_sum


def phi_function(x: float):
    return (1/math.sqrt(2*math.pi))*math.exp((-x**2)/2);
