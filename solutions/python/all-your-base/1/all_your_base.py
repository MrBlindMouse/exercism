"""Base conversion"""

def rebase(input_base, digits, output_base):
    """Convert digit from one base to another

    :param input_base: int - The base of the supplied digits
    :param digits: [int] - The digits to be converted
    :param outbut_base - The base that the supplied digits needs to be converted to
    :return: str - The converted digits
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= int(digit) < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    digits.reverse()
    value = sum((digits[pos] * input_base**pos) for pos in range(len(digits)))

    if value == 0:
        return [0]

    new_digits = []
    while value > 0:
        new_digits.append(value % output_base)
        value = value // output_base
    new_digits.reverse()

    return new_digits
