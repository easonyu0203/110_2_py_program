from typing import List


def get_sign_index(words: list[str]) -> int:
    for sign in "+-":
        try:
            index = words.index(sign)
            return index
        except ValueError:
            continue
    return -1


def get_number(words: list[str], sign_index: int) -> int:
    # is sign index second last word?
    if sign_index + 2 != len(words):
        return -1
    try:
        number = int(words[sign_index+1])
        if number < 0:
            return -1
    except ValueError:
        return -1


class Request:
    _amount: int
    _is_valid: bool
    _name: str

    def __init__(self, line: str):
        # variables declare
        self._line = line
        self._is_valid = False
        self._name = ""
        self._amount = 0

        # set variables
        # split line to words
        words: list[str] = self._line.strip().split()
        # get sign index
        sign_index = get_sign_index(words)
        if sign_index == -1:
            return
        # get number
        number = get_number(words, sign_index)


def main() -> None:
    pass


if __name__ == '__main__':
    # main()
    s = "".join(["a"])
    print(s)

