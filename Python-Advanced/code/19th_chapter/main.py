from typing import Generator

#example from python documentation
def echo_round() -> Generator[int, float, str]:
    res = yield
    while res:
        res = yield round(res)
    return "OK"



def simple_generator() -> Generator[str,None,None]:
    generator_str = "Hello World"
    yield generator_str
    generator_str += "!"
    yield generator_str

def main():
    for value in simple_generator():
        print(value)

if __name__ == "__main__":
    main()