def multiply_all(*args: int) -> int:
    result = 1
    for n in args:
        result *= n
    return result

if __name__ == '__main__':
    print(multiply_all(-2, 13, 4))
    print(multiply_all(20))
    print(multiply_all())