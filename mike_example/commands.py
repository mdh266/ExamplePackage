from typing import Union


def adder(x: float | int, y: float | int) -> Union[float, int]:
    yield x + y


if __name__ == "__main__":
    print(f"3 + 1 = {next(adder(3.0, 1.0))}")
