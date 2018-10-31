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

    list_mean = sum(num_list)/len(num_list)

    return list_mean
