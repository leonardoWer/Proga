import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    matrix = []
    for i in range(0, len(values), n):
        matrix.append(values[i:i + n])

    return matrix


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    res = []
    for row in grid:
        res.append(str(row[pos[-1]]))
    return res


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    res = []
    """
    Размеры квадратов по индексам
    0-2
    3-5
    6-8
    """
    # Если в первой строке квадратов
    if str(pos[0]) in "012":
        for row in range(3):
            # Если в первом квадрате
            if str(pos[-1]) in "012":
                res.extend(grid[row][0:3])
            # Если во втором квадрате
            if str(pos[-1]) in "345":
                res.extend(grid[row][3:6])
            # Если в третьем квадрате
            if str(pos[-1]) in "678":
                res.extend(grid[row][6:9])

    # Если во второй строке квадратов
    if str(pos[0]) in "345":
        for row in range(3, 6):
            # Если в первом квадрате
            if str(pos[-1]) in "012":
                res.extend(grid[row][0:3])
            # Если во втором квадрате
            if str(pos[-1]) in "345":
                res.extend(grid[row][3:6])
            # Если в третьем квадрате
            if str(pos[-1]) in "678":
                res.extend(grid[row][6:9])

    # Если в третьей строке квадратов
    if str(pos[0]) in "678":
        for row in range(6, 9):
            # Если в первом квадрате
            if str(pos[-1]) in "012":
                res.extend(grid[row][0:3])
            # Если во втором квадрате
            if str(pos[-1]) in "345":
                res.extend(grid[row][3:6])
            # Если в третьем квадрате
            if str(pos[-1]) in "678":
                res.extend(grid[row][6:9])

    return res


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    False
    """
    for row in grid:
        for el in row:
            if el == ".":
                return grid.index(row), row.index(el)
    return False


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    values = []
    for possible_number in "123456789":
        if possible_number not in get_row(grid, pos) and possible_number not in get_col(grid, pos) and possible_number not in get_block(grid, pos):
            values.append(possible_number)
    return set(values)


def check_position_is_safe(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int], el) -> bool:
    """Возвращает 1 если на заданное место можно поставить заданный элемент, 0 если нет"""
    return (el not in get_row(grid, pos)) and (el not in get_col(grid, pos)) and (el not in get_block(grid, pos))


def grid_solution(grid: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    """
    Возвращает результат решения пазла
     >>> grid = read_sudoku('puzzle1.txt')
     >>> grid_solution(grid)
     [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    solve(grid)
    return grid


def solve(grid: tp.List[tp.List[str]]):
    """
    Решение пазла, заданного в grid
    - Возвращает 1, когда пазл решён, и 0, если нет
     >>> grid = read_sudoku('puzzle1.txt')
     >>> solve(grid)
     True
    """
    # Если нет пустых клеток, возвращаем 1, то есть флаг, что пазл решён
    if not find_empty_positions(grid):
        return True
    # Находим пустую клетку
    empty_position = find_empty_positions(grid)
    # Находим возможные значения
    mb_values = find_possible_values(grid, empty_position)
    # Если таких нет, возвращаем ноль
    if len(mb_values) == 0:
        return False
    else:
        for el in mb_values:
            """
            Если после подстановки цифры на заданное место она не будет повторяться ни в строке, ни в столбце, ни в блоке
            То ставим цифру на это место
            """
            if check_position_is_safe(grid, empty_position, el):
                grid[empty_position[0]][empty_position[1]] = el
                # Если теперь пазл решён, возвращаем 1
                if solve(grid):
                    return True
                # Если нет, заменяем значение обратно на точку
                grid[empty_position[0]][empty_position[1]] = "."
        # Если ни один элемент не подошёл, возвращаем 0
        return False


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False
    >>> solution = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    >>> check_solution(solution)
    True
    >>> solution = [['3', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    >>> check_solution(solution)
    False
    """
    for row in range(9):
        for col in range(9):
            pos = (row, col)
            if len(set(get_row(solution, pos))) != 9 or len(set(get_col(solution, pos))) != 9 or len(set(get_block(solution, pos))) != 9:
                return False
    return True


def generate_random_grid(grid: tp.List[tp.List[str]]):
    if not find_empty_positions(grid):
        return True
    # Находим пустую клетку
    empty_position = find_empty_positions(grid)
    row, col = empty_position[0], empty_position[1]
    for cnt in range(9):
        random_number = str(random.randint(1, 9))
        if check_position_is_safe(grid, empty_position, random_number):
            grid[row][col] = random_number
            if generate_random_grid(grid):
                return True

            grid[row][col] = "."

    return False


def delete_cells(grid:tp.List[tp.List[str]], cnt_del_el: int):
    while cnt_del_el:
        row = random.randint(0,8)
        col = random.randint(0, 8)
        if grid[row][col] != ".":
            grid[row][col] = "."
            cnt_del_el -=1


def generate_sudoku(cnt_el: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = grid_solution(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = grid_solution(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = grid_solution(grid)
    >>> check_solution(solution)
    True
    """
    if cnt_el>81:
        cnt_el = 81
    cnt_del_el = 81-cnt_el
    grid = read_sudoku("empty_puzzle.txt")
    generate_random_grid(grid)
    delete_cells(grid, cnt_del_el)
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        print(f"Original sudoku {fname}")
        display(grid)
        solution = grid_solution(grid)
        if check_solution(solution):
            print("Puzzle successful solved")
            if not solve(grid):
                print(f"Puzzle {fname} can't be solved, mb it incorrect")
            else:
                print(f"Solve sudoku {fname}")
                display(solution)
        else:
            print("Hmm, probably program is not perfect, because solution not right\n")
