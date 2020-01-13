import re
PAIR_RE = re.compile(r'''
    (
        \d+     # Any number of digits
    )
    (?:         # A group of
        -       # A single dash
        (\d+)   # Any number of digits
    )?          # That last dash and number are optional
''', re.VERBOSE)

def parse_ranges(ranges_string):
    """Return iterable based on comma-separated numeric ranges."""
    pairs = (
        ((a, b) if b else (a, a))
        for a, b in PAIR_RE.findall(ranges_string)
    )
    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop)+1)
    )