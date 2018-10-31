"""
string_util.py
Sample repository for MolSSI Workshop at SERMACS.

Misc. string processing functions
"""

def title_case(sentence):
    """
    Convert string to title case.
    Title case means that the first character of every word is capitalized, otherwise lowercase.


    Parameters
    --------------
    sentence: string
        Sentence to be converted to title case

    Returns:
    --------------
    ret: string
        Input string in title case

    Examples
    ---------
    >>> title_case('ThIs iS a StrIng tO be ConVerted')
        'This Is A String To Be Converted'
    """

    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()

    return ret
