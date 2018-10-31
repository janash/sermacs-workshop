"""
molssi_math.py
Sample repository for MolSSI Workshop at SERMACS.

Misc. math functions
"""


def mean(num_list):
    """
    Computes the mean of a list of numbers.

    Parameters
    ---------------
    num_list: list
        List to calculate mean of

    Returns
    --------------
    list_mean: float
        Mean of list of numbers
    """

    # Check that input is type list
    if not isinstance(num_list, list):
        raise TypeError('Input must be type list')

    # Check that list has length
    if len(num_list) == 0:
        raise ZeroDivisionError('Cannot calculate mean of empty list')

    # Check that values in list are numeric
    try:
        list_mean = sum(num_list) / len(num_list)
    except TypeError:
        raise TypeError('Values of list must be type int or float')

    return list_mean
