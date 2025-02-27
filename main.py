from interval_series_task import make_task2
from nums import get_first_task_nums, get_second_nums
from prob_plotting import boxplot_for_two_lists
from variation_series_task import make_task1

PRECISION = 4

if __name__ == "__main__":
    make_task1(PRECISION)
    make_task2(PRECISION)

    boxplot_for_two_lists(
        get_first_task_nums(), get_second_nums(), "tex/output/boxplot.pdf"
    )
