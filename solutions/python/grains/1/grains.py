"""Grain Counting"""

def square(number):
    """Calculate the number of grains on the square
    :param number: int - Number of the square
    :return: int - Returns the number of grains
    """
    if not 0 < number < 65:
        raise ValueError('square must be between 1 and 64')
    grain = 1
    for i in range(number-1):
        grain = grain * 2
    return grain

CHESSBOARD = 64
def total():
    """Calculate the total number of grain
    :return: int - Returns the number of grains
    """
    return sum(square(i+1) for i in range(CHESSBOARD))
