import sys
import doctest
def return_digits(number):
    r"""
    str -> None
    >>> return_digits("1345") #doctest: +ELLIPSIS
    ' 1  333    4...'
    """
    Zero = ["  ***  ",
            " *   * ",
            "*     *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "]
    One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
    Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
    Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
    Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
    Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
    Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
    Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
    Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
    Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
    Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

    try:
        digits = number
        row = 0
        ln = ""
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                numb = ""
                for i in digit[row]:
                    numb = digit[row].replace("*",str(number))
                line += numb
                column += 1
            row += 1
            ln = ln + line +"\n"
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)
    return ln


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            numb = ""
            for i in digit[row]:
                numb = digit[row].replace("*",str(number))
            line += numb
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)