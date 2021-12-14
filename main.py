def find_min(numbers):
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def sum_of_numbers(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def multiplication_of_numbers(numbers):
    result = 1
    # в данном случае overflow error не может появиться т.к. есть несколько вариантов:
    # 1. мы сразу считали очень большое число при переводе из строки и тогда мы получим inf
    # 2. мы получаем inf ( превышение допустимого значения числа ) перемножением -> не получим ошибку
    # overflow error возникает только в случае возведения некоторого числа float в степень, т.к. там именно там
    # стоит проверка на переполнение
    for number in numbers:
        result *= number
    return result


def get_numbers_from_file(filename):
    f = None
    numbers = []
    try:
        f = open(filename, 'r')
    except FileNotFoundError as e:
        print('No such file.')
        return -1
    data = f.read()
    f.close()
    try:
        numbers = list(map(float, data.split()))
    except Exception as e:
        print('Unexpected data type, check your file.')
        return -1
    return numbers


def main():
    filename = input('Enter filename to proceed: ')
    numbers = get_numbers_from_file(filename)
    if numbers == -1:
        exit()
    print(multiplication_of_numbers(numbers))


if __name__ == '__main__':
    main()
