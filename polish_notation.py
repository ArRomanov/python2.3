def calculate_notation():
    notation = input("Введите выражение польской нотации:\n")
    chars = notation.strip().split(' ')
    operator = chars.pop(0)
    nums = chars.copy()
    assert len(operator) + len(nums) == 3, 'Количество введенных символов отличается от 3'
    assert operator in ('+', '-', '*', '/'), f'Первый оператор "{operator}" не является одним из множества +, -, *, /'
    try:
        nums = [int(nums[0]), int(nums[1])]
    except ValueError:
        print('Проблема с преобразованием символа в число')

    if operator == '+':
        result = nums[0] + nums[1]
    elif operator == '-':
        result = nums[0] - nums[1]
    elif operator == '*':
        result = nums[0] * nums[1]
    elif operator == '/':
        try:
            result = nums[0] / nums[1]
        except TypeError:
            print('Строки нельзя делить')
            exit()
    print(result)


if __name__ == "__main__":
    calculate_notation()
