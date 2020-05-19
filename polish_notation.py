def calculate_notation():
    notation = input("Введите выражение польской нотации:\n")
    chars = notation.split(' ')
    operators = [char for char in chars if char and not char.isdigit()]
    assert operators[-1] in ('+', '-', '*', '/'), 'Первый оператор не является одним из множества +, -, *, /'
    nums = [int(char) for char in chars if char.isdigit()]
    assert len(nums) - len(operators) == 1, f'Количество операторов и цифр не соответствует. Цифр - {len(nums)}, операторов - {len(operators)}'

    result = nums.pop(0)
    try:
        for operator in reversed(operators):
            second_num = nums.pop(0)
            if operator == '+':
                result += second_num
                continue
            elif operator == '-':
                result -= second_num
                continue
            elif operator == '*':
                result *= second_num
                continue
            elif operator == '/':
                result /= second_num
                continue
            else:
                raise AssertionError(f'Данный оператор не обрабатывается - "{operator}"')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        exit()
    except TypeError as ex:
        print(f'Недопустимое действие c переменной - {ex}')
        exit()
    print(result)


if __name__ == "__main__":
    calculate_notation()
