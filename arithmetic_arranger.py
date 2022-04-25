from typing import List, Dict


def arrange_rows(problem: str, symbol: str) -> dict or None:
    problems_dict: Dict[str, str, str, int] = {'first_row': '', 'second_row': '', 'symbol': '', 'result': int}
    operand1: int
    operand2: int

    if symbol in problem:
        number_list = problem.split(f' {symbol} ')
        operand1 = int(number_list[0])
        operand2 = int(number_list[1])
        for index in range(len(number_list)):
            keys = list(problems_dict)
            problems_dict[keys[index]] += number_list[index]
            problems_dict['symbol'] = symbol
    else:
        return None

    if symbol == '+':
        problems_dict['result'] = operand1 + operand2
    else:
        problems_dict['result'] = operand1 - operand2

    return problems_dict


def validate_input(problems: list) -> None:
    if len(problems) > 5:
        raise Exception('Error: Too many problems.')

    for index in range(len(problems)):
        if '*' in problems[index]:
            raise Exception('Error: Operator must be "+" or "-".')

        if '/' in problems[index]:
            raise Exception('Error: Operator must be "+" or "-".')

        if '+' in problems[index]:
            numbers = problems[index].split(' + ')

            if (len(numbers[0])) > 4:
                raise Exception('Error: Numbers cannot be more than four digits.')

            if (len(numbers[1])) > 4:
                raise Exception('Error: Numbers cannot be more than four digits.')

            if type(int(numbers[0])) is not int:
                raise Exception('Error: Numbers must only contain digits.')

            if type(int(numbers[1])) is not int:
                raise Exception('Error: Numbers must only contain digits.')

        if '-' in problems:
            numbers = problems[index].split(' - ')

            if (len(numbers[0])) > 4:
                raise Exception('Error: Numbers cannot be more than four digits.')

            if (len(numbers[1])) > 4:
                raise Exception('Error: Numbers cannot be more than four digits.')

            if type(int(numbers[0])) is not int:
                raise Exception('Error: Numbers must only contain digits.')

            if type(int(numbers[1])) is not int:
                raise Exception('Error: Numbers must only contain digits.')


def arithmetic_arranger(problems: list, answers: bool = False) -> None:
    # Verify that the problems array is the correct length.
    validate_input(problems)

    # Creates variables and lists
    rows_dict: List[dict] = []
    problem_list: List[dict] = []
    first_line: str = ''
    second_line: str = ''
    third_line: str = ''
    fourth_line: str = ''
    display_string: str = ''
    line: str = '------'
    space: str = '    '  # exactly 4 spaces.

    # Loops through problem list and arrange the problem numbers in order.
    for problem in problems:
        sum_dictionary = arrange_rows(problem, '+')
        subst_dictionary = arrange_rows(problem, '-')

        if sum_dictionary is not None:
            rows_dict.append(sum_dictionary)

        if subst_dictionary is not None:
            rows_dict.append(subst_dictionary)

    # Construct string that will have all the problems laid out
    for index in range(len(rows_dict)):
        symbol: str = rows_dict[index]['symbol']

        problem_dict: Dict[str, str, str, int] = {
            'operand1': rows_dict[index]['first_row'],
            'operand2': rows_dict[index]['second_row'],
            # 'symbol': rows_dict[index]['symbol']
            'result': str(rows_dict[index]['result'])
        }

        # Each problem will be their own dictionary with their each operand having their correct number of spaces
        if len(problem_dict['operand1']) == 1:
            problem_dict['operand1'] = '  ' + problem_dict['operand1']

        if len(problem_dict['operand2']) == 1:
            problem_dict['operand2'] = '  ' + problem_dict['operand2']

        if len(problem_dict['result']) == 1:
            problem_dict['result'] = '  ' + problem_dict['result']

        if len(problem_dict['operand1']) == 2:
            problem_dict['operand1'] = '    ' + problem_dict['operand1']

        if len(problem_dict['operand2']) == 2:
            problem_dict['operand2'] = ' ' + problem_dict['operand2']

        if len(problem_dict['result']) == 2:
            problem_dict['result'] = '    ' + problem_dict['result']

        if len(problem_dict['operand1']) == 3:
            problem_dict['operand1'] = ' ' + problem_dict['operand1']

        if len(problem_dict['operand2']) == 3:
            problem_dict['operand2'] = ' ' + problem_dict['operand2']

        if len(problem_dict['result']) == 3:
            problem_dict['result'] = '   ' + problem_dict['result']

        if len(problem_dict['operand1']) == 4:
            problem_dict['operand1'] = '  ' + problem_dict['operand1']

        if len(problem_dict['operand1']) == 4:
            problem_dict['operand1'] = '  ' + problem_dict['operand1']

        if len(problem_dict['result']) == 4:
            problem_dict['result'] = '  ' + problem_dict['result']

        problem_dict['operand2'] = f'{symbol} ' + problem_dict['operand2']

        problem_list.append(problem_dict)

    # Makes the lines before logging them into the console.
    for index in range(len(problem_list)):
        first_line += problem_list[index]['operand1'] + space

        second_line += problem_list[index]['operand2'] + space
        third_line += line + space

        if answers is True:
            fourth_line += problem_list[index]['result'] + space

    first_line += '\n'
    second_line += '\n'
    third_line += '\n'

    display_string = first_line + second_line + third_line + fourth_line

    # Displays the problems
    print(display_string)

    # return arranged_problems
