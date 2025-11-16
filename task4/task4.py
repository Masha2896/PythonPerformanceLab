import sys


def main():
    if len(sys.argv) < 2:
        print("Ошибка: Укажите имя файла в аргументе командной строки.")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            nums = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return
    except ValueError:
        print("Ошибка: Некорректные данные. Все значения должны быть целыми числами.")
        return

    nums.sort()
    n = len(nums)

    if n == 0:
        print(0)
        return

    median = nums[n // 2]

    total_moves = 0
    for num in nums:
        total_moves += abs(num - median)

    if total_moves <= 20:
        print(total_moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу.")

if __name__ == "__main__":
    main()