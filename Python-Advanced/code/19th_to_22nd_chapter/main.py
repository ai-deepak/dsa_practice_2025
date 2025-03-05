from typing import Generator

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