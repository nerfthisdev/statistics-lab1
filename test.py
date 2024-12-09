

from sample_functions import get_inverse_laplace


# print(get_inverse_laplace(0.495 + 0.5))
print(get_confidence_interval_for_expvalue(
    get_expected_value_estimate(nums),
    len(nums),
    get_sample_standard_deviation_corrected(nums, get_expected_value_estimate(nums)),
    0.9
))
