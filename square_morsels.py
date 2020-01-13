import cmath

def is_perfect_square(number, *, complex=False):
    """Return True if given number is the square of an integer."""
    if complex:
        root = cmath.sqrt(number)
        return root.real.is_integer() and root.imag.is_integer()
    if number < 0:
        return False
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number