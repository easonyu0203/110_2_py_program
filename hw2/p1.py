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
        number = int(words[sign_index + 1])
        if number < 0:
            return -1
    except ValueError:
        return -1
    return number


def split_to_worlds(line: str) -> list[str]:
    words = [s for s in line]
    sign_index = get_sign_index(words)
    if sign_index == -1:
        raise ValueError()
    return ["".join(words[:sign_index]).strip(), words[sign_index], "".join((words[sign_index+1:])).strip()]


class Request:
    _amount: int
    _is_valid: bool
    _name: str

    log_level: bool = True

    @classmethod
    def log(cls, s: str):
        if Request.log_level:
            print(s)

    def __init__(self, line: str):
        # variables declare
        self._line = line
        self._is_valid = False
        self._name = ""
        self._amount = 0

        # set variables
        # split line to words
        try:
            words: list[str] = split_to_worlds(self._line)
        except ValueError:
            return
        Request.log(f"words: {words}")
        # get sign index
        sign_index = get_sign_index(words)
        Request.log(f"sign_index: {sign_index}")
        if sign_index == -1:
            return
        # get number
        number = get_number(words, sign_index)
        Request.log(f"number: {number}")


def main() -> None:
    pass


if __name__ == '__main__':
    # main()
    Request("巧克力   +10")
