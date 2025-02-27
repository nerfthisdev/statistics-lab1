import math
from variation_series import (
    get_expected_value_estimate,
    get_inverse_laplace,
    get_sample_standard_deviation_corrected,
    get_variation_series,
)


def dict_to_latex_table_str(data: dict[any, any]) -> str:
    dict_len = len(data.keys())

    column_count = dict_len if dict_len < 10 else 10

    output = "\\begin{tabular}{|" + "|".join(["c"] * column_count) + "|}\n"
    count = 0
    key_row: list[str] = []
    value_row: list[str] = []

    for key, value in data.items():
        count += 1

        key_row.append(str(key))
        value_row.append(str(value))

        if count % column_count == 0 or count == dict_len:
            output += f"    \\hline\n"
            output += f"    {' & '.join(key_row)}\\\\\n"
            output += f"    \\hline\n"
            output += f"    {' & '.join(value_row)}\\\\\n"
            output += f"    \\hline\n"

            key_row.clear()
            value_row.clear()

            if count != dict_len - 1:
                output += f"    [1ex]\n"

    output += "\\end{tabular}"
    return output


def get_latex_form_empirical_distribution_func(nums: list[float], func) -> str:
    sorted_nums = get_variation_series(set(nums))

    output = "F^*(x) = \\begin{cases}\n"
    output += f"    0.0, x < {sorted_nums[0]}\\\\\n"
    for i in range(len(sorted_nums) - 1):
        output += f"    {round(func(sorted_nums[i+1]), 10)},\\quad {sorted_nums[i]} \\leq x < {sorted_nums[i+1]} \\\\\n"
    output += f"    1.0,\\quad x \\geq {sorted_nums[-1]} \\\\\n"
    output += "\\end{cases}\n"
    return output


def get_confidence_interval_for_expvalue_large_set_with_latex_steps(
    average_value: float, n: int, sigma: float, confidence_prob: float
) -> tuple[float, float]:
    output = "$$ \\gamma = " + str(confidence_prob) + " $$\n"
    output += "$$ \\overline{x} = " + str(average_value) + " $$\n"
    output += "$$ \\sigma = " + str(sigma) + " $$\n"

    t = get_inverse_laplace(confidence_prob / 2 + 0.5)
    output += "$$ \\t_{\\frac{\\gamma+1}{2}} = " + str(t) + " $$\n"
    varepsilon = t * sigma / math.sqrt(n)
    output += "$$ \\varepsilon = " + str(varepsilon) + " $$\n"

    output += f"$$ ({average_value - varepsilon}, {average_value + varepsilon}) $$\n"
    return output


def get_latex_form_empirical_distribution_func(nums: list[float], func) -> str:
    sorted_nums = get_variation_series(set(nums))

    output = "F^*(x) = \n"
    output += f"    0.0, x < {sorted_nums[0]}\n"
    for i in range(len(sorted_nums) - 1):
        output += f"    {round(func(sorted_nums[i+1]), 2)},  {sorted_nums[i]} <= x < {sorted_nums[i+1]} \n"
    output += f"    1.0, x >= {sorted_nums[-1]} \n"
    return output


def compute_table_to_latex_table_str_to_file(dict, path):
    with open(path, "w") as f:
        output = compute_table_to_latex_table_str(dict)
        f.write(output)


def compute_table_to_latex_table_str(data: dict[any, any]) -> str:
    # height = len(data.keys())
    width = len(data[1].keys()) + 1

    output = "\\begin{tabular}{|" + "|".join(["c"] * width) + "|}\n"
    output += f"    \\hline\n"
    output += f"    i & {' & '.join(f'${x}$' for x in data[1].keys())}\\\\\n"
    output += f"    \\hline\n"
    for key, value in data.items():
        output += (
            f"    {key} & {' & '.join([f'${x}$' for x in data[key].values()])}\\\\\n"
        )
        output += f"    \\hline\n"

    output += "\\end{tabular}"
    return output
