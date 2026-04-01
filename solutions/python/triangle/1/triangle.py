"""Triangle Checks"""

def equilateral(sides):
    """Checks if Triangle is Equilatiral
    :param sides: [float] - List with 3 side lengths
    :return: bool - True if Triangle is Equilateral
    """
    if not is_triangle(sides):
        return False
    return sides[0]==sides[1]==sides[2]


def isosceles(sides):
    """Checks if Triangle is Isosceles
    :param sides: [float] - List with 3 side lengths
    :return: bool - True if Triangle is Isosceles 
    """
    if not is_triangle(sides):
        return False
    return len(set(sides)) <= 2


def scalene(sides):
    """Checks if Triangle is Equilatiral
    :param sides: [float] - List with 3 side lengths
    :return: bool - True if Triangle is Scalene 
    """
    if not is_triangle(sides):
        return False
    return sides[0] != sides[1] != sides[2] != sides[0]

def is_triangle(sides):
    """Checks if Triangle
    :param sides: [float] - List with 3 side lengths
    :return: bool - True if Triangle
    """
    if len(sides) != 3:
        return False
    sides.sort()
    return (
        (sides[0]+sides[1]) > sides[2]
        and all(side > 0 for side in sides)
    )

