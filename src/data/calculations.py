def calculate_correlation_matrix(data, method):
    """
    :param data: dataset
    :param method: pearson, spearman, kendall
    :return: correlation matrix
    """
    # Calculate the correlation matrix
    correlation_matrix = data.corr(
        method=method
    )

    return correlation_matrix