from sample_functions import get_variation_series

def dict_to_latex_table_str(data: dict[any, any]) -> str:
    table_size = 10
    dict_len = len(data.keys());

    output = "\\begin{tabular}{|" + "|".join(["c"]*dict_len) + "|}\n"
    count = 0
    key_row: list[str] = []
    value_row: list[str] = []

    for key, value in data.items():
        count += 1

        key_row.append(str(key))
        value_row.append(str(value))

        if (count % table_size == 0 or count == dict_len):
            output += f"    \\hline\n"
            output += f"    {' & '.join(key_row)}\\\\\n"
            output += f"    \\hline\n"
            output += f"    {' & '.join(value_row)}\\\\\n"
            output += f"    \\hline\n"

            key_row.clear()
            value_row.clear()

            if (count != dict_len - 1):
                output += f"    [1ex]\n"

    output += "\\end{tabular}"
    return output

def get_latex_form_empirical_distribution_func(nums: list[float], func) -> str:
    sorted_nums = get_variation_series(set(nums))

    output = "F^*(x) = \\begin{cases}\n"
    output +=f"0, x < {sorted_nums[0]}\\\\\n"
    for i in range(len(sorted_nums) - 1):
        output += f"    {round(func(sorted_nums[i]), 3)},\\quad {sorted_nums[i]} \\leq x < {sorted_nums[i+1]} \\\\\n"
    output += f"    1,\\quad x \\geq {sorted_nums[-1]} \\\\\n"
    output += "\\end{cases}\n"
    return output
