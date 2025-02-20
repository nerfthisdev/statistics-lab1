
# path_to_statistical_interval_series_tex = "tex/output/statistical_interval_series.tex"
# with open(path_to_statistical_interval_series_tex, "w") as f:
#     output = dict_to_latex_table_str(
#         get_statistical_interval_series(
#             get_whole_range_with_offsets(nums),
#             get_interval_count_by_sturgess(len(nums)),
#             nums))

    # f.write(output)
# print(f"Интервальный ряд: записаны в {path_to_statistical_interval_series_tex}")


# path_to_statistical_interval_series_test_tex = f"tex/output/statistical_interval_series_{bin_count}_bins.tex"
# with open(path_to_statistical_interval_series_test_tex, "w") as f:
#     output = dict_to_latex_table_str(get_statistical_interval_series(get_whole_range(nums), bin_count, nums))
#     f.write(output)
# print(f"Интервальный статистический ряд: записаны в {path_to_statistical_interval_series_test_tex}")

# plot_histogram_with_sturgess(nums, "tex/output/histogram_sturgess.png")

# bin_count = 8

# plot_histogram(
#     get_whole_range(nums),
#     bin_count,
#     nums,
#     f"tex/output/histogram_{bin_count}_bins.png"
# )

# plot_cumulative(
#     get_whole_range(nums),
#     bin_count,
#     nums,
#     f"tex/output/cumulative_{bin_count}_bins.png"
# )
