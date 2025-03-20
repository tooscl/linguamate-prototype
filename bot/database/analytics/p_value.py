import scipy.stats as stats


def calculate_p_value(success_a, total_a, success_b, total_b):
    p_a = success_a / total_a
    p_b = success_b / total_b
    pooled_prob = (success_a + success_b) / (total_a + total_b)

    z = (p_a - p_b) / (pooled_prob * (1 - pooled_prob) * (1 / total_a + 1 / total_b)) ** 0.5
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # Двусторонний тест
    return p_value