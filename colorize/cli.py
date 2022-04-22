import sys
import re
import random
import zlib


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
color_codes = {
    #    "Black": "0;30",
    #    "Dark Gray": "1;30",
    "Red": "0;31",
    "Light Red": "1;31",
    "Green": "0;32",
    "Light Green": "1;32",
    "Brown/Orange": "0;33",
    "Yellow": "1;33",
    "Blue": "0;34",
    "Light Blue": "1;34",
    "Purple": "0;35",
    "Light Purple": "1;35",
    "Cyan": "0;36",
    "Light Cyan": "1;36",
    #    "Light Gray": "0;37",
    #    "White": "1;37"
}
colors = sorted(set(color_codes.values()))


def apply_color(code):
    return '\033[' + code + 'm'


def main():
    random.seed(42)

    if len(sys.argv) > 1:
        regexp = sys.argv[1]
    else:
        print("""This utility will highlight matched strings in stdin.

Just specify regexp as its argument.

If you don't like distribution of the colors, add some random number as second argument.
""")
        exit(-1)

    if len(sys.argv) > 2:
        skew = int(sys.argv[2])
    else:
        skew = 0

    m = re.compile(regexp)

    tab = dict()
    def color(tok):
        if tok not in tab:
            key = (zlib.adler32(bytes(tok, 'utf-8')) + skew) % len(colors)
            tab[tok] = colors[key]
        return tab[tok]

    for line in sys.stdin:
        line = line.rstrip()
        toks = list(set(m.findall(line)))
        for tok in toks:
            line = line.replace(tok, apply_color(color(tok)) + tok + NC)
        print(line)


if __name__ == '__main__':
    main()
